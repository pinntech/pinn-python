"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester


class EnrollmentKey(object):
    """Interface to create an enrollment key."""

    OBJECT_NAME = 'enrollment_key'
    endpoint = '/v1/enrollment_keys'

    def __init__(self, response):
        """Initialize an enrollment_key model with an API response."""
        self.response = response
        self.enrollment_key_id = response['enrollment_key_id']
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.expires_at = response['expires_at']
        self.object = response['object']
        self.livemode = response['livemode']
        self.secret = response['secret']

    def __str__(self):
        return json.dumps(self.response, indent=4, sort_keys=True, separators=(',', ': '))

    @classmethod
    def create(cls, user_id):
        """Create a new enrollment key for a given user."""
        data = {'user_id': user_id}
        return EnrollmentKey(Requester.post(cls.endpoint, data=data))
