#! venv/bin/python3

import boto3
import os

from constants import BUCKET_NAME

s3 = boto3.resource("s3")

# Build a list of all the .py files in this folder (non-recursive)
files = [
    f
    for f in os.listdir(".")
    if f.endswith(".py") or f.endswith(".txt") or f.endswith(".html")
]

bucket = s3.Bucket(BUCKET_NAME)
for f in files:
    # bucket.upload_file(f, f) # local filename, object key
    bucket.upload_file(
        f, f, ExtraArgs={"ACL": "public-read", "ContentType": "text/html"}
    )  # upload with public access

# https://nh-python-bucket.s3.amazonaws.com/requirements.txt
# https://nh-python-bucket.s3.amazonaws.com/sample.html
