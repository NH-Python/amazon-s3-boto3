#! venv/bin/python3
from constants import BUCKET_NAME

import boto3
import pprint

s3 = boto3.resource("s3")
# s3.create_bucket(Bucket=BUCKET_NAME)

## Create a publicly-readable bucket
s3.create_bucket(Bucket=BUCKET_NAME, ACL="public-read")
