"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from .list import List
from .device import Device
from .log import Log
from ..requester import Requester


class User(object):
    """Methods to create, list, retrieve, update or delete users."""

    OBJECT_NAME = 'user'
    endpoint = '/v1/users'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.authenticated_at = response['authenticated_at']
        self.device_enrolled = response['device_enrolled']
        self.left_palm_enrolled = response['left_palm_enrolled']
        self.right_palm_enrolled = response['right_palm_enrolled']
        self.object = response['object']
        self.metadata = response['metadata']

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    def dump(self):
        """Dump the model to a dictionary, method matches to json.dump() behavior"""
        return {'user_id': self.user_id,
                'created_at': self.created_at,
                'object': self.object,
                'metadata': self.metadata}

    @classmethod
    def create(cls, metadata=None):
        """Create a new Pinn user."""
        if metadata:
            data = {'metadata': metadata}
        else:
            data = None
        return User(Requester.post(cls.endpoint, data=data))

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn users."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, User, limit)

    @classmethod
    def list_devices(cls, user_id, limit=None, starting_after=None):
        """List created Pinn user's devices."""
        endpoint = cls.endpoint + '/' + user_id + '/devices'
        response = Requester.get(endpoint, params={'limit': limit,
                                                   'starting_after': starting_after})
        return List(response, Device, limit)

    @classmethod
    def list_logs(cls, user_id, limit=None, starting_after=None):
        """List created Pinn users."""
        endpoint = cls.endpoint + '/' + user_id + '/logs'
        response = Requester.get(endpoint, params={'limit': limit,
                                                   'starting_after': starting_after})
        return List(response, Log, limit)

    @classmethod
    def retrieve(cls, user_id):
        """Retrieve a user with a provided user ID."""
        return User(Requester.get(cls.endpoint + '/' + user_id))

    @classmethod
    def update(cls, user_id, metadata, status):
        """Update the metadata for a user."""
        data = {}
        if metadata:
            data['metadata'] = metadata
        if status:
            data['status'] = status
        return User(Requester.patch(cls.endpoint + '/' + user_id, data=data))

    @classmethod
    def delete(cls, user_id):
        """Delete a user with the given user ID."""
        return Requester.delete(cls.endpoint + '/' + user_id)
