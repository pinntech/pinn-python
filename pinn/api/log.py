"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from ..requester import Requester
from .list import List


class Log(object):
    """Methods to create, list, retrieve, update or delete users."""

    OBJECT_NAME = 'log'
    endpoint = '/v1/logs'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.log_id = response['log_id']
        self.user_id = response['user_id']
        self.device_id = response['device_id']
        self.created_at = response['created_at']
        self.success = response['success']
        self.score = response['score']
        self.factors = response['factors']
        self.auth_type = response['auth_type']
        self.object = response['object']
        self.app_id = response['app_id']
        self.web_app_id = response['web_app_id']

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn logs."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, Log, limit)

    @classmethod
    def retrieve(cls, log_id):
        """Retrieve a log with a provided log ID."""
        return Log(Requester.get(cls.endpoint + '/' + log_id))
