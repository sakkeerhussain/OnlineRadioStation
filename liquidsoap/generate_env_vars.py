import os

icecast_source_password = os.environ.get('ICECAST_SOURCE_PASSWORD', 'password')
liquidsoap_source_password = os.environ.get('LIQUIDSOAP_SOURCE_PASSWORD', 'password')

file = open('env-vars.sh', 'w')
file.write(f'export ICECAST_SOURCE_PASSWORD="{icecast_source_password}"\n')
file.write(f'export LIQUIDSOAP_SOURCE_PASSWORD="{liquidsoap_source_password}"\n')
file.close()