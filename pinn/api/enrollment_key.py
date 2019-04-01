"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester


class EnrollmentKey(object):
    """Enrollment Key resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        enrollment_key_id (str): Unique ID for this enrollment key
        user_id (str): ID of the user who the key corresponds to
        created_at (int): Unix timestamp in seconds for when the key was created
        expires_at (int): Unix timestamp in seconds for when the key will expire
        livemode (bool): True if enrollment key is in live environment
        secret (str): A secret to authenticate the enroll request from Pinn mobile SDK
    """

    OBJECT_NAME = 'enrollment_key'
    endpoint = '/v1/enrollment_keys'

    def __init__(self, response):
        """Initialize an enrollment_key model with an API response."""
        self.response = response
        self.object = response['object']
        self.enrollment_key_id = response['enrollment_key_id']
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.expires_at = response['expires_at']
        self.livemode = response['livemode']
        self.secret = response['secret']

    def __str__(self):
        return json.dumps(self.response, indent=4, sort_keys=True, separators=(',', ': '))

    @classmethod
    def create(cls, user_id):
        """Create a new enrollment key for a given user.

        This key is used as proof that your system is authorizing a given
        Pinn user to enroll. You MUST ensure proper trust is established between
        the user and your service before performing this operation.

        Args:
            user_id (str): The ID of the Pinn user being authorized to enroll.

        Returns:
            EnrollmentKey: A special purpose key to authorize enrollment

        Raises:
            pinn.errors.RequestFailedError: User with ID supplied does not exist
            pinn.errors.APIError: Internal server error
            pinn.errors.APIConnectionError: API is unreachable [501-503]
        """
        data = {'user_id': user_id}
        return EnrollmentKey(Requester.post(cls.endpoint, data=data))
