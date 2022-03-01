# Online Radio Station

An online radio station setup using icecast and liquidsoap with dockerised setup.

## Environment Variables
Name                       | Description                                                              | Default Value
---------------------------|--------------------------------------------------------------------------| ---------------
ICECAST_ADMIN_PASSWORD     | The admin password for icecast server admin portal.                      | password
ICECAST_SOURCE_PASSWORD    | The password used to authenticate icecast stream source, like liquidsoap.| password
ICECAST_RELAY_PASSWORD     | Icecast relay password                                                   | password
LIQUIDSOAP_SOURCE_PASSWORD | The password used to authenticate live stream mic to liquidsoap server.  | password
DJANGO_SECRET              | The secret value used in the django server running inside.               | django-insecure-secret
ADMIN_PASSWORD             | The password used to login to the web admin UI                           | password

## How to run
1. Update icecast admin password in environment variable 'ICECAST_ADMIN_PASSWORD' otherwise will default to 'password' 
2. Update icecast source password in environment variable 'ICECAST_SOURCE_PASSWORD' otherwise will default to 'password'
3. Update icecast relay password in environment variable 'ICECAST_RELAY_PASSWORD' otherwise will default to 'password'
3. Update liquidsoap source password in environment variable 'LIQUIDSOAP_SOURCE_PASSWORD' otherwise will default to 'password'
4. Update django secret in environment variable 'DJANGO_SECRET' otherwise will be defaulted to 'django-insecure-secret'
4. Update admin password in environment variable 'ADMIN_PASSWORD' otherwise will be defaulted to 'password'
5. Run the ./setup.sh file in terminal after setting up the docker container.


## Access Details

### Icecast:
- Access URL: http://localhost:8000
- Stream URL: http://localhost:8000/stream
- Username: admin
- Password: Loads from env variable 'ICECAST_ADMIN_PASSWORD' or 'password'

### Admin Web UI:
- Access URL: http://localhost:5000
- Username: admin
- Password: Loads from env variable 'ADMIN_PASSWORD' or 'password'
 
### Connect Live Mic:
- Server Address: localhost
- Server Port: 8080
- Mount point: /mount
- Username: source
- Password: Loads from env variable 'LIQUIDSOAP_SOURCE_PASSWORD' or 'password'

TODO Items:
1. Create super user if not existing
2. Make host configurable in liquidsoap
3. Make ports configurable
4. add API_SERVER_HOST to readme
5. Upload media files to S3 in API server
6. Install database seperatly and update
4. add ICECAST_SERVER_HOST to readme