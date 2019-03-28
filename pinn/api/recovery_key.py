"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

import json
from ..requester import Requester


class RecoveryKey(object):
    """Interface to create an enrollment key."""

    OBJECT_NAME = 'recovery_key'
    endpoint = '/v1/recovery_keys'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.response = response
        self.recovery_key_id = response['recovery_key_id']
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.expires_at = response['expires_at']
        self.object = response['object']
        self.livemode = response['livemode']
        self.secret = response['secret']
        self.flow = response['flow']

    def __str__(self):
        return json.dumps(self.response, indent=4, sort_keys=True, separators=(',', ': '))

    @classmethod
    def create(cls, user_id, flow):
        """Create a new enrollment key for a given user."""
        data = {'user_id': user_id, 'flow': flow}
        return RecoveryKey(Requester.post(cls.endpoint, data=data))
