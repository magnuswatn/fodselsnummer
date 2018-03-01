fodselsnummer
=============

.. image:: https://travis-ci.org/magnuswatn/fodselsnummer.svg?branch=master
    :target: https://travis-ci.org/magnuswatn/fodselsnummer

.. image:: https://codecov.io/gh/magnuswatn/fodselsnummer/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/magnuswatn/fodselsnummer

.. image:: https://badge.fury.io/py/fodselsnummer.svg
    :target: https://badge.fury.io/py/fodselsnummer

Used to generate and validate Norwegian birth numbers ("fødselsnummer").

Installation
------------

.. code-block:: bash

    $ pipenv install fodselsnummer



Example usage
-------------

.. code-block:: python

    import fodselsnummer

    fodselsnummer.check_fnr('12345678900')
