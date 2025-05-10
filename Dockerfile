FROM ubuntu:20.04

ENV TZ=Europe/Berlin
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./app /app
EXPOSE 80
ENTRYPOINT [ "python3" ]

CMD [ "gevent_prod.py" ]