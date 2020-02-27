#! venv/bin/python3

import boto3

s3 = boto3.resource("s3")

for bucket in s3.buckets.all():
    print(f"{bucket.name:45}{bucket.creation_date}")
