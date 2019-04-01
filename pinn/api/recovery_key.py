"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester


class RecoveryKey(object):
    """Recovery key resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        recovery_key_id (str): Unique ID for this recovery key
        user_id (str): ID of the user who the key corresponds to
        created_at (int): Unix timestamp in seconds for when the key was created
        expires_at (int): Unix timestamp in seconds for when the key will expire
        livemode (bool): True if recovery key is in live environment
        secret (str): A secret to authenticate the recovery request from Pinn mobile SDK
        flow (list): The auth flow required for recovery
    """

    OBJECT_NAME = 'recovery_key'
    endpoint = '/v1/recovery_keys'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.response = response
        self.object = response['object']
        self.recovery_key_id = response['recovery_key_id']
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.expires_at = response['expires_at']
        self.livemode = response['livemode']
        self.secret = response['secret']
        self.flow = response['flow']

    def __str__(self):
        return json.dumps(self.response, indent=4, sort_keys=True, separators=(',', ': '))

    @classmethod
    def create(cls, user_id, flow):
        """Create a new recovery key for a given user.

        Args:
            user_id (str): ID of user to create the recovery key for.
            flow (list, optional): List of remote factors to check prior to re-enrollment

        Returns:
            RecoveryKey: The newly created recovery key

        Raises:
            pinn.errors.RequestFailedError: User not found, invalid `flow` provided
            pinn.errors.APIError: Internal server error
            pinn.errors.APIConnectionError: API is unreachable [501-503]
        """
        data = {'user_id': user_id, 'flow': flow}
        return RecoveryKey(Requester.post(cls.endpoint, data=data))
