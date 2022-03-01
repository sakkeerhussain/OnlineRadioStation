FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get install -y icecast2
COPY ./config.xml /etc/icecast2/icecast.xml
COPY ./start.sh ./start.sh
RUN chmod +x ./start.sh

EXPOSE 80

CMD ["./start.sh"]

