"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

import json
from ..requester import Requester


class Key(object):
    """Methods to create, list, retrieve, update or delete keys."""

    OBJECT_NAME = 'key'
    endpoint = '/users/{}/keys'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.key_id = response['key_id']
        # self.type = response['type']
        self.created_at = response['created_at']
        self.object = response['object']
        self.metadata = response['metadata']

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    def dump(self):
        """Dump the model to a dictionary, method matches to json.dump() behavior"""
        return {'key_id': self.key_id,
                # 'type': self.type,
                'created_at': self.created_at,
                'object': self.object,
                'metadata': self.metadata}

    @classmethod
    def create(cls, user_id, public_key, metadata=None):
        """Add key to the user's keychain."""
        data = {'public_key': public_key}
        if metadata:
            data['metadata'] = metadata
        return Key(Requester.post(cls.endpoint.format(user_id), data=data))

    @classmethod
    def list(cls, user_id):
        """List all keys in the user's keychain."""
        return [Key(key) for key in Requester.get(cls.endpoint.format(user_id))]

    @classmethod
    def retrieve(cls, user_id, key_id):
        """Retrieve a specific key for a given user."""
        return Key(Requester.get(cls.endpoint.format(user_id) + '/' + key_id))

    @classmethod
    def delete(cls, user_id, key_id):
        """Remove a key from the user's keychain."""
        return Requester.delete(cls.endpoint.format(user_id) + '/' + key_id)
