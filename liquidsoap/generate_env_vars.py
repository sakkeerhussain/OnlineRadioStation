import os

icecast_source_password = os.environ.get('ICECAST_SOURCE_PASSWORD', 'password')
liquidsoap_source_password = os.environ.get('LIQUIDSOAP_SOURCE_PASSWORD', 'password')

file = open('.env', 'w')
file.write(f'ICECAST_SOURCE_PASSWORD={icecast_source_password}\n')
file.write(f'LIQUIDSOAP_SOURCE_PASSWORD={liquidsoap_source_password}\n')
file.close()