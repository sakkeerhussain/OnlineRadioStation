import os

icecast_source_password = os.environ.get('ICECAST_SOURCE_PASSWORD', 'password')
liquidsoap_source_password = os.environ.get('LIQUIDSOAP_SOURCE_PASSWORD', 'password')
api_server_host = os.environ.get('API_SERVER_HOST', 'http://host.docker.internal:5000')
icecast_server_host = os.environ.get('ICECAST_SERVER_HOST', 'host.docker.internal')

file = open('.env', 'w')
file.write(f'ICECAST_SOURCE_PASSWORD={icecast_source_password}\n')
file.write(f'LIQUIDSOAP_SOURCE_PASSWORD={liquidsoap_source_password}\n')
file.write(f'API_SERVER_HOST={api_server_host}\n')
file.write(f'ICECAST_SERVER_HOST={icecast_server_host}\n')
file.close()