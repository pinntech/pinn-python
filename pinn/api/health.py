"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from ..requester import Requester
from ..errors import PinnError


def healthy():
    """Perform a health check against the configured Pinn host.

    Returns:
        bool: True if host is available, False otherwise
    """

    endpoint = '/health'

    try:
        Requester.get(endpoint)
        return True
    except PinnError:
        return False
