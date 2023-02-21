import boto3

bucket="my-s3-bucket-ab"

s3_bucket = boto3.client(bucket)
s3_bucket.list_objects_v2(bucket=bucket, prefix='maze')