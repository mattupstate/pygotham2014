Basic Docker + Python App Example
=================================

This folder contains a very basic Python application and accompanying `Dockerfile` to illustrate
how one can use Docker_ to control a development environment. The application is essentially a
"Hello, World" web app built with Flask. Additionally, there is a test suite to illustrate how
one might use py.test_ to run the tests in the context of a Docker container.


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


Instructions
------------

1. Build the Docker image:

    $ docker build -t pygotham/app1 .

2. Test the image:

    $ docker run --rm -it -p 5000:5000 pygotham/app1

3. Test the app is running:

    $ curl http://$DOCKER_IP:5000

4. Run the tests in the context of the Docker container

    $ docker run --rm -it -v $(pwd):/code pygotham/app1 py.test tests

.. _Docker http://docker.com
.. _py.test http://pytest.org
