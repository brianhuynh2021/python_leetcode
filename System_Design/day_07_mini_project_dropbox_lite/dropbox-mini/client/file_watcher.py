import hashlib
import os
import time
from datetime import datetime
from pathlib import Path

import requests
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class DropboxClient:
    def __init__(self, base_url: str, token: str, watch_folder: str):
        self.base_url = base_url
        self.token = token
        self.watch_folder = Path(watch_folder)
        self.headers = {"Authorization": f"Bearer {token}"}
        self.last_sync_time = datetime.utcnow()

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file"""
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # 64KB chunks
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()

    def upload_file(self, file_path: Path):
        """Upload file to server"""
        file_size = file_path.stat().st_size
        file_hash = self.calculate_file_hash(file_path)
        relative_path = file_path.relative_to(self.watch_folder)

        # Initialize upload
        init_response = requests.post(
            f"{self.base_url}/upload/init",
            headers=self.headers,
            json={
                "file_name": file_path.name,
                "file_size": file_size,
                "file_hash": file_hash,
                "file_path": str(relative_path.parent),
            },
        )

        if init_response.status_code != 200:
            print(f"Failed to initialize upload: {init_response.text}")
            return

        init_data = init_response.json()

        if init_data.get("deduplication"):
            print(f"File {file_path.name} already exists (deduplication)")
            return

        # Upload chunks
        chunk_size = init_data["chunk_size"]
        version_id = init_data["version_id"]

        with open(file_path, "rb") as f:
            chunk_index = 0
            while True:
                chunk_data = f.read(chunk_size)
                if not chunk_data:
                    break

                chunk_hash = hashlib.sha256(chunk_data).hexdigest()

                files = {"chunk_file": (f"chunk_{chunk_index}", chunk_data)}
                data = {
                    "version_id": version_id,
                    "chunk_index": chunk_index,
                    "chunk_hash": chunk_hash,
                }

                chunk_response = requests.post(
                    f"{self.base_url}/upload/chunk",
                    headers=self.headers,
                    data=data,
                    files=files,
                )

                if chunk_response.status_code != 200:
                    print(
                        f"Failed to upload chunk {chunk_index}: {chunk_response.text}"
                    )
                    return

                print(f"Uploaded chunk {chunk_index} of {file_path.name}")
                chunk_index += 1

        # Complete upload
        complete_response = requests.post(
            f"{self.base_url}/upload/complete/{version_id}", headers=self.headers
        )

        if complete_response.status_code == 200:
            print(f"Successfully uploaded {file_path.name}")
        else:
            print(f"Failed to complete upload: {complete_response.text}")

    def download_file(self, file_id: str, file_name: str):
        """Download file from server"""
        response = requests.get(
            f"{self.base_url}/download/{file_id}", headers=self.headers, stream=True
        )

        if response.status_code != 200:
            print(f"Failed to download {file_name}")
            return

        file_path = self.watch_folder / file_name
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded {file_name}")

    def sync_delta(self):
        """Get and apply changes from server"""
        response = requests.get(
            f"{self.base_url}/sync/delta",
            headers=self.headers,
            params={"since": self.last_sync_time.isoformat()},
        )

        if response.status_code != 200:
            print(f"Failed to get sync delta: {response.text}")
            return

        data = response.json()
        for change in data["changes"]:
            if change["action"] == "created" or change["action"] == "modified":
                self.download_file(change["file_id"], change["file_name"])
            elif change["action"] == "deleted":
                file_path = self.watch_folder / change["file_name"]
                if file_path.exists():
                    file_path.unlink()
                    print(f"Deleted {change['file_name']}")

        self.last_sync_time = datetime.fromisoformat(data["last_sync_time"])


class FileWatcher(FileSystemEventHandler):
    def __init__(self, client: DropboxClient):
        self.client = client

    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")
            time.sleep(0.5)  # Wait for file to be fully written
            self.client.upload_file(Path(event.src_path))

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
            time.sleep(0.5)
            self.client.upload_file(Path(event.src_path))


def main():
    # Configuration
    BASE_URL = os.getenv("DROPBOX_API_URL", "http://localhost:8003")
    TOKEN = os.getenv("DROPBOX_TOKEN")
    WATCH_FOLDER = os.getenv("WATCH_FOLDER", "./dropbox_sync")

    if not TOKEN:
        print("Error: DROPBOX_TOKEN environment variable not set")
        return

    # Create watch folder if not exists
    Path(WATCH_FOLDER).mkdir(exist_ok=True)

    # Initialize client
    client = DropboxClient(BASE_URL, TOKEN, WATCH_FOLDER)

    # Setup file watcher
    event_handler = FileWatcher(client)
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=True)
    observer.start()

    print(f"Watching folder: {WATCH_FOLDER}")
    print("Press Ctrl+C to stop...")

    try:
        while True:
            # Periodic sync
            client.sync_delta()
            time.sleep(30)  # Sync every 30 seconds
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
