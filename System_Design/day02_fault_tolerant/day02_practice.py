```python
import time
import random

class UploadError(Exception):
    pass

def upload_to_storage(image_data):
    """Simulates a flaky upload process"""
    if random.random() < 0.6:
        raise UploadError("Simulated upload failure")
    return "Image uploaded successfully."

def upload_with_retry(image_data, max_retries=3):
    backoff = 1

    for attempt in range(1, max_retries + 1):
        try:
            result = upload_to_storage(image_data)
            print(f"✅ Success on attempt {attempt}")
            return result
        except UploadError as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt == max_retries:
                print("❌ All retries failed.")
                return "Upload failed"
            print(f"⏳ Backing off for {backoff} seconds...")
            time.sleep(backoff)
            backoff *= 2

# Simulate test
if __name__ == "__main__":
    fake_image = b"binary-image-data"
    print(upload_with_retry(fake_image))