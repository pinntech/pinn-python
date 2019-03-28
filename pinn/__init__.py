"""
pinn
----
Python bindings for the Pinn REST API

Get started with:
    >>> import pinn
    >>> pinn.secret_key = "sk_eAtrbzTaZMSaGGCPzToL804DjxNMnudO"
    >>> pinn.User.create()

:copyright: (c) 2019 Pinn Technologies, Inc.
:license: All rights reserved
"""

import os

# Package Information
# -------------------
__title__ = 'pinn'
__author__ = 'Pinn Technologies, Inc.'
__license__ = 'All rights reserved'
__copyright__ = 'Copyright 2019 Pinn Technologies, Inc.'

# Configuration Variables
# -----------------------
secret_key = os.environ.get('PINN_SECRET_KEY', None)
api_host = os.environ.get('PINN_API_HOST', 'https://pinnapis.com')
api_version = os.environ.get('PINN_API_VERSION', None)

# API
# ---
from .api.user import User  # NOQA
from .api.enrollment import Enrollment  # NOQA
from .api.verification import Verification  # NOQA
from .api.key import Key  # NOQA
from .api.enrollment_key import EnrollmentKey  # NOQA
from .api.recovery_key import RecoveryKey  # NOQA
from .utils import IDToken  # NOQA

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
