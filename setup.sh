#!/bin/sh

cd icecast || exit
sh ./build-and-run.sh

cd ../liquidsoap || exit
sh ./build-and-run.sh

cd ../api_server || exit
sh ./build-and-run.sh