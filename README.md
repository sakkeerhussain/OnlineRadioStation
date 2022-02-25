# Online Radio Station

An online radio station setup using icecast and liquidsoap with dockerised setup.


## How to run
1. Update icecast admin password in environment variable 'ICECAST_ADMIN_PASSWORD' otherwise will default to 'password' 
2. Update icecast source password in environment variable 'ICECAST_SOURCE_PASSWORD' otherwise will default to 'password'
3. Update icecast relay password in environment variable 'ICECAST_RELAY_PASSWORD' otherwise will default to 'password'
4. Run the ./setup.sh file in terminal after setting up the docker container.
