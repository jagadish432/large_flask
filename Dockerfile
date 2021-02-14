FROM ubuntu:latest
MAINTAINER jaggu4329 <jagadish.dachepalli@gmail.com>

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential && apt-get install curl -y && apt-get install vim -y

COPY book-rental-calculator/ /book-rental-calculator

RUN pip3 install -r /book-rental-calculator/requirements.txt

WORKDIR /book-rental-calculator/

EXPOSE 5020

RUN ls -al

CMD ["sh", "dev.sh"]
