docker build -t online-radio:latest .
docker run -it -p 80:8080 -p 8000:9000 online-radio:latest /bin/sh

