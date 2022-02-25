FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get install -y liquidsoap
COPY ./script.liq ./script.liq
ADD ./music ./music

COPY ./start.sh ./start.sh
RUN chmod +x ./start.sh
RUN mkdir log

COPY ./env-vars.sh ./env-vars.sh
RUN source ./env-vars.sh

EXPOSE 8080

CMD ["./start.sh"]
