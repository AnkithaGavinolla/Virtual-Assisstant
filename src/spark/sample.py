# print('a')
import boto3
client=boto3.resource('s3')
bucket=client.Bucket('productmetadataankitha')
for obj in bucket.objects.all():
    key=obj.key
    body=obj.get()['Body'].read(100)
    print(body)
    print(key)