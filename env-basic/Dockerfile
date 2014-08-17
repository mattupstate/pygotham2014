FROM ubuntu:14.04.1

RUN apt-get update -y
RUN apt-get -y dist-upgrade
RUN apt-get upgrade -y
RUN apt-get install -yq python-dev python-pip

ADD . /code
WORKDIR /code

RUN pip install -q -e ./

EXPOSE 5000

CMD python wsgi.py
