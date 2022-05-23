FROM ubuntu:18.04
MAINTAINER chandra.sutrisno@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app /app

WORKDIR /app/

CMD ["gunicorn3", "-b", "0.0.0.0:8080", "app1:app", "--workers=3"]