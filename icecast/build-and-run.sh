#!/bin/sh

python3 ./generate_config.py

docker build -t online-radio-icecast:latest .
docker stop online-radio-icecast
docker run -d --rm -p 80:80 --name online-radio-icecast online-radio-icecast:latest
