#!/bin/sh

set -o allexport
source ../env-vars.yml
set +o allexport

python3 ./generate_config.py

docker build -t online-radio-icecast:latest .
docker stop online-radio-icecast
docker run -d --rm -p 8000:8000 --name online-radio-icecast online-radio-icecast:latest
