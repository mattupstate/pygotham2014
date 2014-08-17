Basic Docker + Python App + Fig Example
=======================================

This folder contains a very basic Python application and accompanying `Dockerfile` to illustrate
how one can use Docker_ to control a development environment with some help from Fig_ to manage a
database dependency. The application goes one step further than the `env-basic` example in this
repository and includes a basic database connection.


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

1. Install Fig:

    $ pip install fig

2. Build the Docker image for the `web` service defined in `fig.yml`:

    $ fig build web

3. Test that the environment variables will be available in the `web` service:

    $ fig run web env

4. Run the `web` service with Fig:

    $ fig run web

5. Test the `web` service is running correctly:

    $ curl http://$DOCKER_IP:5000

4. Run the tests in the context of the `web` service container

    $ fig run web py.test tests


.. _Fig http://fig.sh
.. _Docker http://docker.com
.. _py.test http://pytest.org
