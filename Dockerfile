# syntax=docker/dockerfile:1

FROM python:3.10.1-bullseye

WORKDIR /app

USER root

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get -y update
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#============================================
# Python App
#============================================
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

USER 1200

CMD [ "python3", "-m" , "scraper.py"]