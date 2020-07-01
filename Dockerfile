FROM ubuntu:latest

RUN apt update -y && apt upgrade -y
RUN apt install python3-pip -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
