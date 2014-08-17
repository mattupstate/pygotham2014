Production Ready Pythong App w/ Docker
======================================

This folder contains a very basic Python application and accompanying `Dockerfile` to illustrate
how one can make a basic Flask app more suited for production deployment.


Getting Started
---------------

This project assumes you have Docker installed to manage your development environment. If you're on
OS X and using boot2docker, it is recommended to setup a shared folder via `these instructions
<https://coderwall.com/p/fvfjyg/>`_ so that files from your local computer may be mounted to a
Docker container. Additionally, I recommend setting an environment variable to the IP address of
the VM Docker is running on. For example:

    $ export DOCKER_IP=192.168.59.103

If you're on Linux simply replace any instances of `DOCKER_IP` in the following commands to
`localhost` or `127.0.0.1`.


Notes
-----

This Docker image, in addition to the Flask application code, also includes installations for
_Nginx and _uWSGI which are, what I would consider, excellent choices to make your Flask/wsgi
applicaiton production ready. There are two accompanying configuration files for Nginx and uWSGI
that ensure that both services log to stdout which is generally considered a good practice for
Docker. Lastly, there is a run script that runs both Nginx and uWSGI in the foreground.


Instructions
------------

1. Build the Docker image:

    $ docker build -t pygotham/app2 .

2. Test the image:

    $ docker run --rm -it -p 80:80 pygotham/app2

3. Test the app is running:

    $ curl http://$DOCKER_IP


.. Nginx http://nginx.org
.. uWSGI http://uwsgi-docs.readthedocs.org
.. _Docker http://docker.com
.. _py.test http://pytest.org
