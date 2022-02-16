#!/bin/sh
python3 -m http.server 9000 & icecast2 -c etc/icecast2/icecast.xml & liquidsoap ./liquidsoap/script.liq