FROM python:3.7-slim-buster

WORKDIR /bot
#install pytelegrambot,mysql-connector-python
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .