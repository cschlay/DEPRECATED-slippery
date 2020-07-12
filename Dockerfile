FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install gcc -y
RUN apt install python3-pip -y
RUN apt install python3-dev -y
RUN apt install libpq-dev -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
RUN python3 manage.py migrate
