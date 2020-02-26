#! venv/bin/python3

import boto3
import os

from constants import BUCKET_NAME

s3 = boto3.resource('s3')

# Build a list of all the .py files in this folder (non-recursive)
files = [py_file for py_file in os.listdir(".") if py_file.endswith(".py")]

bucket = s3.Bucket(BUCKET_NAME)
for py_file in files:
    bucket.upload_file(py_file, py_file) # local filename, object key