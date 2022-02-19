#!/bin/sh


# docker build -t online-radio:latest .

# Kill previous running docker
# docker stop online-radio
# docker rm online-radio

# docker run -d --rm -p 5000:5000 --name online-radio online-radio:latest


cd icecast
sh ./build-and-run.sh

cd ../liquidsoap
sh ./build-and-run.sh