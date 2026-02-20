import boto3
from botocore.client import Config as BotoConfig
from common.config import Config


class S3Client:
    def __init__(self):
        self.client = boto3.client(
            "s3",
            endpoint_url=Config.S3_ENDPOINT,
            aws_access_key_id=Config.S3_ACCESS_KEY,
            aws_secret_access_key=Config.S3_SECRET_KEY,
            config=BotoConfig(signature_version="s3v4"),
        )
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        try:
            self.client.head_bucket(Bucket=Config.S3_BUCKET)
        except:
            self.client.create_bucket(Bucket=Config.S3_BUCKET)

    def upload_chunk(self, chunk_data: bytes, object_key: str):
        self.client.put_object(Bucket=Config.S3_BUCKET, Key=object_key, Body=chunk_data)

    def download_chunk(self, object_key: str):
        response = self.client.get_object(Bucket=Config.S3_BUCKET, Key=object_key)
        return response["Body"].read()

    def generate_presigned_url(self, object_key: str, expiration=3600):
        return self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": Config.S3_BUCKET, "Key": object_key},
            ExpiresIn=expiration,
        )

    def delete_object(self, object_key: str):
        self.client.delete_object(Bucket=Config.S3_BUCKET, Key=object_key)


s3_client = S3Client()
