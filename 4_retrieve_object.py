#! venv/bin/python3

import boto3
import os

from constants import BUCKET_NAME

s3 = boto3.resource('s3')
OBJECT_KEY = "list_objects.py"

obj = s3.Object(BUCKET_NAME, OBJECT_KEY)

# 'Body' is of type 'StreamingBody'
# Can read in chunks, or in entirity.  We're reading the whole thing.
response = obj.get()
print(response['Body'].read().decode('utf-8'))

#obj.download_file("downloaded_list_objects.py")