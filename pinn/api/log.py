"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from ..requester import Requester
from .list import List


class Log(object):
    """Log resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        log_id (str): Unique ID for the log
        user_id (str): ID of the user that authenticated
        device_id (str): ID of the device that authenticated
        app_id (str): ID of the mobile app that was involved
        web_app_id (str, optional): ID of web app that was involved
        created_at (int): Unix timestamp in seconds for when the app was created
        success (bool): True if authentication was successful
        score (float): Combined score for all scorable biometrics
        factors (dict): Breakdown of all factors used an their score if applicable
        auth_type (str): Either `web` or `mobile`
    """

    OBJECT_NAME = 'log'
    endpoint = '/v1/logs'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.response = response
        self.object = response['object']
        self.log_id = response['log_id']
        self.user_id = response['user_id']
        self.device_id = response['device_id']
        self.app_id = response['app_id']
        self.web_app_id = response['web_app_id']
        self.created_at = response['created_at']
        self.success = response['success']
        self.score = response['score']
        self.factors = response['factors']
        self.auth_type = response['auth_type']

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
