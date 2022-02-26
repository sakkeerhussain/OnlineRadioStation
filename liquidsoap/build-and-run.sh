#!/bin/sh

python3 ./generate_env_vars.py

docker build -t online-radio-liquidsoap:latest .
docker stop online-radio-liquidsoap
docker rm online-radio-liquidsoap
docker run -d --rm -p 8080:8080 --env-file .env --name online-radio-liquidsoap online-radio-liquidsoap:latest
