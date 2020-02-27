#! venv/bin/python3
from constants import BUCKET_NAME

import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket(BUCKET_NAME)
# Inefficent way to delete versions
for v in bucket.object_versions.all():
    v.delete()
bucket.delete()
