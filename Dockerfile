FROM ubuntu 
MAINTAINER demousr@gmail.com 

RUN apt-get update 
RUN apt-get install -y icecast2
COPY ./icecast/config.xml /etc/icecast2/icecast.xml
RUN service icecast2 start

RUN apt-get install -y curl


CMD ["echo", "testing..."] 

