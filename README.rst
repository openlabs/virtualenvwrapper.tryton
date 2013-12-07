Tryton template for virtualenvwrapper
=====================================

Tryton template for virtualenvwrapper to be used with the `mkproject`
command.

Installation
------------

::

  pip install virtualenvwrapper.tryton


Usage
-----

::

  mkproject -t tryton tryton_project


This command would install the current development version of tryton. The
mercurial repository of tryton trunk will be cloned to the root of your
project too.

You can use the same extension to make development environments with older
versions of Tryton too. For example to make a development environment for
2.8 version of tryton use::

  mkproject -t tryton28 tryton_project


The project folder also has an etc folder and the `trytond.conf` template
which you could use in your project.

Templates
---------

The templates included are:

* tryton30 - Tryton 3.0
* tryton28 - Tryton 2.8
* tryton26 - Tryton 2.6
* tryton24 - Tryton 2.4
* tryton22 - Tryton 2.2
* tryton20 - Tryton 2.0
* tryton18 - Tryton 1.8
* tryton16 - Tryton 1.6
* tryton14 - Tryton 1.4
* tryton12 - Tryton 1.2
* tryton10 - Tryton 1.0
