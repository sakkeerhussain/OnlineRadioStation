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
file.close()
