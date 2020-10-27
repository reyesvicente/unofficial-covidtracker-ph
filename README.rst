Unofficial COVID-19 Tracker Philippines
=======================================

This is an unofficial tracker for the Philippines. A side project to
enhance my skill in using APIs, Digital Ocean deployment and Docker.

Installation
------------

This web app uses
`Cookiecutter-Django <cookiecutter-django.readthedocs.io/>`__,
`Docker <https://docker.com>`__, `Digital
Ocean <https://m.do.co/c/8773beb85774>`__ for hosting, `Contextual News
API <https://rakuten.net>`__ and the `US Web Design
System <https://designsystem.digital.gov/>`__.

Running in you localhost is easy with ``docker-compose``. Check the
`official cookiecutter-django
docks <https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html>`__
on how to run it locally with docker.

.. code:: bash

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up

Use
`this <https://codeburst.io/a-full-deployment-of-cookiecutter-django-on-digitalocean-with-docker-5293f31a1fdc?source=rss----61061eb0c96b---4>`__
guide for deploying the app to `Digital
Ocean <https://m.do.co/c/8773beb85774>`__\ (affiliate link). Use the
affiliate link to get $100 for 2 months in Digital Ocean.

Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

The app has not been tested. I've only used Django's testing tools hence
will only test this using the said testing tools.

If you like this project, consider buying me a
`coffee <https://www.buymeacoffee.com/highcenburg>`__.

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`__
