#! venv/bin/python3
from constants import BUCKET_NAME

import boto3
import pprint

s3 = boto3.resource('s3')
try:
    s3.create_bucket(Bucket=BUCKET_NAME)
except Exception as ex:
    pprint(ex)