.. figure::  _static/pinn-python-logo.png
   :align:   center

   Python library bindings for the Pinn REST API

Installation
============

The easiest way to install is by using PyPi, either directly or within your requirements.txt::
    
    pip install --upgrade pinn

You can also install directly from source::

    python setup.py install

Configuration
=============

Now that you have the package properly installed, you can configure the library with your
Pinn secret key. If you don't have access, first reach out to sales@pinn.ai.

You may set the ``secret_key`` value directly (convenient for shell testing), but typically you
should set ``PINN_SECRET_KEY`` as an environmental variable for the package to pick up
automatically.

Directly set the key like so::

    >>> import pinn
    >>> pinn.secret_key = 'sk_H5dqd648Ix9vJ7J70NjRlhXyP6AouUx8'

Or, set your environment variable for the library to autoload::

    $ export PINN_SECRET_KEY=sk_H5dqd648Ix9vJ7J70NjRlhXyP6AouUx8

Now you're all set to start making API calls.

API Reference
=============

.. automodule:: pinn
    :members: secret_key, api_host, api_version

Resources
---------

.. autoclass:: pinn.User

Errors
------

.. automodule:: pinn.errors
    :members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Utilities
---------

Other
-----

.. autofunction:: pinn.healthy

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
