import boto3

ssm = boto3.client('ssm', region_name='us-east-2')

def get_param(name, decrypt=False):
    return ssm.get_parameter(Name=name, WithDecryption=decrypt)['Parameter']['Value']

# Prueba de parámetros
debug = get_param('DEBUG')
allowed_hosts = get_param('ALLOWED_HOSTS')
secret_key = get_param('AWS_SECRET_ACCESS_KEY', decrypt=True)

print("DEBUG =", debug)
print("ALLOWED_HOSTS =", allowed_hosts)
print("AWS_SECRET_ACCESS_KEY =", secret_key)