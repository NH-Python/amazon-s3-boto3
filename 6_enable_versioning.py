#! venv/bin/python3

import boto3
import os
import pprint
from constants import BUCKET_NAME

s3 = boto3.resource("s3")
bucket_versioning = s3.BucketVersioning(BUCKET_NAME)
response = bucket_versioning.enable()
pprint.pprint(response)
