FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get install -y liquidsoap
COPY ./script.liq ./script.liq
ADD ./music ./music

COPY ./start.sh ./start.sh
RUN chmod +x ./start.sh

EXPOSE 8080

CMD ["./start.sh"]
