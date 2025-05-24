import os
import boto3
from constants import region, file_path, bucket_name


def upload_vocab():

    s3_client = boto3.client('s3', region_name=region)
    s3_resource = boto3.resource('s3')

    buckets = list(s3_resource.buckets.all())
    
    location = {'LocationConstraint': region}

    create_bucket_instance(buckets, s3_client, s3_resource, location)

    key = os.path.basename(file_path)
    bucket = s3_resource.Bucket(bucket_name)

    bucket.upload_file(Filename=file_path, Key=key)



def create_bucket_instance(buckets, s3_client, s3_resource, location):
    if not buckets:
        print("No buckets found, please create a bucket")
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    existing_buckets = [bucket.name for bucket in s3_resource.buckets.all()]

    if bucket_name not in existing_buckets:
        print("Creating the requested bucket right now")
        s3_client.create_bucket(uBcket=bucket_name, CreateBucketConfiguration=location)






