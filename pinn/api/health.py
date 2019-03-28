"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester


class Health(object):
    """Healthy."""

    OBJECT_NAME = 'health'
    endpoint = '/health'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        pass

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    @classmethod
    def retrieve(cls):
        """Retrieve a health."""
        return Requester.get(cls.endpoint)
