from storages.backends.s3boto3 import S3Boto3Storage
from dummy_app.settings import get_param
# from decouple import config

class StaticStorage(S3Boto3Storage):
    location = get_param('STATIC_LOCATION')
    default_acl = 'public-read'
    # custom_domain = f"{get_param('STORAGE_BUCKET_NAME')}.s3.amazonaws.com"
