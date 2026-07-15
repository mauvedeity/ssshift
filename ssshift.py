#!env python3
#
# ssshift
#
# Use boto3 to move files into s3
#
import boto3
import sys, os

def mmmoveit(mfile):
  s3 = boto3.client('s3')
  remote = 'pds/' + os.path.basename(mfile)
  s3.upload_file(
    Filename = mfile,
    Bucket= 'mauvedeity-backup',
    Key = remote
  )

def process(args):  # first one is name of script, second one is name of file to ssshift
  if len(args) == 2:
    mmmoveit(args[1])
  else:
    print(f"usage: {args[0]} <file>\n\tCopies a file to s3")
    exit(1)

if __name__ == '__main__':
  process(sys.argv)
