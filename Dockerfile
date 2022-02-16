FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get install -y icecast2
COPY ./icecast/config.xml /etc/icecast2/icecast.xml

RUN apt-get install -y liquidsoap
ADD ./liquidsoap ./liquidsoap
RUN mkdir -p ./log/liquidsoap/

RUN apt-get install -y python3
RUN python3 --version

COPY ./start-service.sh ./start-service.sh
RUN chmod +x ./start-service.sh

EXPOSE 8000
EXPOSE 9000
EXPOSE 8080

CMD ["./start-service.sh"]
# CMD ["python3", "-m", "http.server", "9000"]
# CMD ["icecast2", "-c", "/etc/icecast2/icecast.xml"]

