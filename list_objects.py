#! venv/bin/python3
from constants import BUCKET_NAME
import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket(BUCKET_NAME)

has_objects = False

for obj in bucket.objects.all():
    print(obj.key)
    has_objects = True

if not has_objects:
    print("No objects in bucket")
