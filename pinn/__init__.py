"""
pinn-python
-----------
Python bindings for the Pinn REST API

Get started with:
    >>> import pinn
    >>> pinn.secret_key = "sk_B4cFkhrMU1WxUQVRs10Naqd"
    >>> pinn.User.create()

:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

import os

# Package Information
# -------------------
__title__ = 'pinn-python'
__version__ = '0.1.0'
__author__ = 'Pinn Technologies, Inc.'
__license__ = 'All rights reserved'
__copyright__ = 'Copyright 2017 Pinn Technologies, Inc.'

# Configuration Variables
# -----------------------
secret_key = os.environ.get('PINN_SECRET_KEY', None)
publishable_key = os.environ.get('PINN_PUBLISHABLE_KEY', None)
api_host = os.environ.get('PINN_API_HOST', 'https://pinnapis.com')
api_version = os.environ.get('PINN_API_VERSION', None)

# Endpoints
# ---------
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
