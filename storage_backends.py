from storages.backends.s3boto3 import S3Boto3Storage
from decouple import config

class StaticStorage(S3Boto3Storage):
    location = config('AWS_STATIC_LOCATION', default='static')
    default_acl = 'public-read'
    custom_domain = f"{config('AWS_STORAGE_BUCKET_NAME')}.s3.amazonaws.com"
