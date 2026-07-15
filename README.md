# ssshift

So you can't use AWS CLI on 32-bit machines any more. Well, all I needed it for was to do a copy from local file
system to s3:

  % aws s3 cp <file> s3://<bucket>/<tag>

So this is using `boto3` to replace just that.

Hence the name.

