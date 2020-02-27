#! venv/bin/python3
from constants import BUCKET_NAME
import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket(BUCKET_NAME)

has_objects = False

for version in bucket.object_versions.all():
    print(f"{version.key:30}{version.version_id:35}{version.is_latest}")
    has_objects = True

if not has_objects:
    print("No objects in bucket")
