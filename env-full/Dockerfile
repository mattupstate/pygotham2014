FROM ubuntu:14.04.1

RUN apt-get update -y
RUN apt-get -y dist-upgrade
RUN apt-get upgrade -y
RUN apt-get install -yq --force-yes python-dev python-pip libpq-dev libpcre3 libpcre3-dev

RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main" > /etc/apt/sources.list.d/nginx.list
RUN apt-get install -yq --force-yes nginx
RUN pip install uwsgi
RUN rm -rf /etc/nginx/nginx.conf /etc/nginx/conf.d /etc/nginx/sites-available /etc/nginx/sites-enabled

ADD . /code
WORKDIR /code
RUN pip install -q -e ./

EXPOSE 80

CMD ./run
