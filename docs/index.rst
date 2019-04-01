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

Basics
======

The library is very straightforward to use. Each resource has at minumum one of the following
CRUDL methods:

* ``create()``
* ``retrieve()``
* ``update()``
* ``delete()``
* ``list()``

For example to create a new Pinn user::

    >>> user = pinn.User.create()
    >>> user.user_id
    'usr_zsWljQAN7p6hBbbi15FXXUJp'

Some time later we can get retrieve the user like so::
    
    >>> user = pinn.User.retrieve(user_id='usr_zsWljQAN7p6hBbbi15FXXUJp')
    >>> user.created_at
    1553984207

Some resources like a User can be updated::

    # You can update the user without retrieving
    >>> user = pinn.User.update(user_id='usr_zsWljQAN7p6hBbbi15FXXUJp',
                                metadata={'external_id': 'ypf3JZpTB5DfByiZt'})
    >>>
    # Or if you already have a User object on hand, you can update the property directly and save
    >>> user.metadata = {'external_id': 'ypf3JZpTB5DfByiZt'}
    >>> user.save()

All resources created under your environment can be deleted, use with extreme caution::

    # Delete the resource when you have an ID on hand
    >>> pinn.User.delete(user_id='usr_zsWljQAN7p6hBbbi15FXXUJp')
    True
    # or delete the resource if you already have it on hand
    >>> user.delete()
    True

Finally listing resources in reverse chronological order::

    >>> pinn.User.list()

Quickstart
==========




Handling Errors
===============


Production Checklist
====================

Once everything is working, take a glance at our checklist here to make sure your implementation
is up to snuff.

- Pinn ``secret_key`` value is stored securely on a server and never in version control
- Pinn ID tokens are always verified before claims are trusted
- Enrollment keys are only issued once user has sufficient privledge within your system
- Pinn errors are all handled for
- The Pinn User ID is mapped to my User resource in a persistent datastore


API Reference
=============

.. automodule:: pinn
    :members: secret_key, api_host, api_version

Resources
---------

User
++++

.. autoclass:: pinn.User
    :members: create, retrieve, update, delete

App
+++

.. autoclass:: pinn.App
    :members: create, retrieve, delete


Device
++++++

.. autoclass:: pinn.Device
    :members: retrieve


Event
+++++

.. autoclass:: pinn.Event


Log
+++

.. autoclass:: pinn.Log


WebhookEndpoint
+++++++++++++++

.. autoclass:: pinn.WebhookEndpoint


EnrollmentKey
+++++++++++++

.. autoclass:: pinn.EnrollmentKey
    :members: create


RecoveryKey
+++++++++++

.. autoclass:: pinn.RecoveryKey
    :members: create

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
