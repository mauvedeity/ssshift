#!env python3
#
# ssshift
#
# Use boto3 to move files into s3
#
import boto3
s3 = boto3.client('s3')
s3.upload_file(
  Filename = 'data.dat',
  Bucket= 'mauvedeity-backup',
  Key = 'folder/data.dat'
)

