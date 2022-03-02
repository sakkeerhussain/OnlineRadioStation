#!/bin/sh

docker build -t online-radio-apiserver:latest .
docker stop online-radio-apiserver
docker run -d --rm -p 5000:5000 --env-file ../.env --name online-radio-apiserver online-radio-apiserver:latest
