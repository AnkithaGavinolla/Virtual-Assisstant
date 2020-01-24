import boto3
s3=boto3.client('s3')
aws_account = boto3.client('sts').get_caller_identity().get('Account')
current_region = boto3.session.Session().region_name
bucket_name1='customerreviewsankitha'
bucket_name2='productmetadataankitha'
bucket_name3='customerqaankitha'
# bucket1=s3.create_bucket(Bucket=bucket_name1,CreateBucketConfiguration={
#         'LocationConstraint': current_region
#     })
# bucket2=s3.create_bucket(Bucket=bucket_name2,CreateBucketConfiguration={
#         'LocationConstraint': current_region
#     })
bucket3=s3.create_bucket(Bucket=bucket_name3,CreateBucketConfiguration={
        'LocationConstraint': current_region
    })
s3.upload_file('/Users/gankitha/Desktop/InsightData/data/meta_Electronics.json',bucket_name2,'/electronics.json')
s3.upload_file('/Users/gankitha/Desktop/InsightData/data/qa_Electronics.json',bucket_name3,'/electronics.json')

