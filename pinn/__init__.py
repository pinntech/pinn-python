"""
pinn
----
Python bindings for the Pinn REST API

Get started with:
    >>> import pinn
    >>> pinn.secret_key = "sk_eAtrbzTaZMSaGGCPzToL804DjxNMnudO"
    >>> pinn.User.create()

:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import os

# Package Information
# -------------------
__title__ = 'pinn'
__author__ = 'Pinn Technologies, Inc.'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Pinn Technologies, Inc.'

# Configuration Variables
# -----------------------
secret_key = os.environ.get('PINN_SECRET_KEY', None)
api_host = os.environ.get('PINN_API_HOST', 'https://pinnapis.com')
api_version = os.environ.get('PINN_API_VERSION', None)

# API
# ---
from .api.app import App  # NOQA
from .api.device import Device  # NOQA
from .api.enrollment_key import EnrollmentKey  # NOQA
from .api.event import Event  # NOQA
from .api.health import Health  # NOQA
from .api.log import Log  # NOQA
from .api.recovery_key import RecoveryKey  # NOQA
from .api.user import User  # NOQA
from .api.webhook_endpoint import WebhookEndpoint  # NOQA
from .utils import IDToken  # NOQA

# Versioning
# ----------
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
