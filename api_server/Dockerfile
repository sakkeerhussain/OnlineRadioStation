FROM ubuntu 
MAINTAINER sakkeerhussainp@gmail.com 

RUN apt-get update 
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-psycopg2

COPY ./requirements.txt ./requirements.txt
COPY ./api_server ./api_server
COPY ./scheduler ./scheduler
COPY ./manage.py ./manage.py
COPY ./start.sh ./start.sh

RUN pip install -r requirements.txt
RUN python3 manage.py migrate

COPY ./start.sh ./start.sh
RUN chmod +x ./start.sh

EXPOSE 5000

CMD ["./start.sh"]
