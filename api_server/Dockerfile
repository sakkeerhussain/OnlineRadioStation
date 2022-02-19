FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt

RUN python3 manage.py migrate

COPY ./start.sh ./start.sh
RUN chmod +x ./start.sh

EXPOSE 5000

CMD ["./start.sh"]
