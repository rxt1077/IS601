FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y firefox-esr
RUN cd /tmp
RUN curl -L -o geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN tar zxvf geckodriver.tar.gz
RUN mv geckodriver /usr/bin/
