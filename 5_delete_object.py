#! venv/bin/python3

import boto3
import os
import pprint
from constants import BUCKET_NAME

s3 = boto3.resource("s3")
OBJECT_KEY = "delete_me.py"

obj = s3.Object(BUCKET_NAME, OBJECT_KEY)
response = obj.delete()
pprint.pprint(response)
