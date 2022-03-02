import os

icecast_source_password = os.environ.get('ICECAST_SOURCE_PASSWORD', 'password')
liquidsoap_source_password = os.environ.get('LIQUIDSOAP_SOURCE_PASSWORD', 'password')
api_server_host = os.environ.get('API_SERVER_HOST', 'http://host.docker.internal:5000')
icecast_server_host = os.environ.get('ICECAST_SERVER_HOST', 'host.docker.internal')
icecast_admin_password = os.environ.get('ICECAST_ADMIN_PASSWORD', 'password')
icecast_relay_password = os.environ.get('ICECAST_RELAY_PASSWORD', 'password')
django_secret = os.environ.get('DJANGO_SECRET')
web_ui_admin_password = os.environ.get('ADMIN_PASSWORD')
backend_database_engine = os.environ.get('BACKEND_DATABASE_ENGINE')
backend_database_name = os.environ.get('BACKEND_DATABASE_NAME')
backend_database_user = os.environ.get('BACKEND_DATABASE_USER')
backend_database_password = os.environ.get('BACKEND_DATABASE_PASSWORD')
backend_database_host = os.environ.get('BACKEND_DATABASE_HOST')
backend_database_port = os.environ.get('BACKEND_DATABASE_PORT')
backend_aws_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
backend_aws_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
backend_aws_file_storage = os.environ.get('DEFAULT_FILE_STORAGE')
backend_aws_bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
backend_aws_s3_region = os.environ.get('AWS_S3_REGION_NAME')


file = open('.env', 'w')
file.write(f'ICECAST_SOURCE_PASSWORD={icecast_source_password}\n')
file.write(f'LIQUIDSOAP_SOURCE_PASSWORD={liquidsoap_source_password}\n')
file.write(f'API_SERVER_HOST={api_server_host}\n')
file.write(f'ICECAST_SERVER_HOST={icecast_server_host}\n')
file.write(f'ICECAST_ADMIN_PASSWORD={icecast_admin_password}\n')
file.write(f'ICECAST_RELAY_PASSWORD={icecast_relay_password}\n')

if django_secret:
    file.write(f'DJANGO_SECRET={django_secret}\n')
if web_ui_admin_password:
    file.write(f'ADMIN_PASSWORD={web_ui_admin_password}\n')
if backend_database_engine:
    file.write(f'BACKEND_DATABASE_ENGINE={backend_database_engine}\n')
if backend_database_name:
    file.write(f'BACKEND_DATABASE_NAME={backend_database_name}\n')
if backend_database_user:
    file.write(f'BACKEND_DATABASE_USER={backend_database_user}\n')
if backend_database_password:
    file.write(f'BACKEND_DATABASE_PASSWORD={backend_database_password}\n')
if backend_database_host:
    file.write(f'BACKEND_DATABASE_HOST={backend_database_host}\n')
if backend_database_port:
    file.write(f'BACKEND_DATABASE_PORT={backend_database_port}\n')

if backend_aws_key_id:
    file.write(f'AWS_ACCESS_KEY_ID={backend_aws_key_id}\n')
if backend_aws_access_key:
    file.write(f'AWS_SECRET_ACCESS_KEY={backend_aws_access_key}\n')
if backend_aws_file_storage:
    file.write(f'DEFAULT_FILE_STORAGE={backend_aws_file_storage}\n')
if backend_aws_bucket_name:
    file.write(f'AWS_STORAGE_BUCKET_NAME={backend_aws_bucket_name}\n')
if backend_aws_s3_region:
    file.write(f'AWS_S3_REGION_NAME={backend_aws_s3_region}\n')

file.close()
