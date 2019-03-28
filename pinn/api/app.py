"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester
from .list import List


class App(object):
    """Methods to create, list, retrieve, update or delete apps."""

    OBJECT_NAME = 'app'
    endpoint = '/v1/apps'

    def __init__(self, response):
        """Initialize a app model with an API response."""
        self.app_id = response['app_id']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.publishable_key = response['publishable_key']
        self.app_type = response['app_type']
        self.name = response['name']
        self.description = response['description']
        self.object = response['object']

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    def dump(self):
        """Dump the model to a dictionary, method matches to json.dump() behavior"""
        return {'app_id': self.app_id,
                'created_at': self.created_at,
                'object': self.object,
                'publishable_key': self.publishable_key,
                'app_type': self.app_type,
                'name': self.name,
                'description': self.description}

    @classmethod
    def create(cls, app_type, name, description=None):
        """Create a new Pinn app."""
        assert app_type in ("android", "ios", "web"), "App must be android, ios, or web"
        data = {'name': name,
                'description': description}
        return App(Requester.post(cls.endpoint + '/' + app_type, data=data))

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn apps."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, App, limit)

    @classmethod
    def retrieve(cls, app_id):
        """Retrieve an app with a provided app ID."""
        return App(Requester.get(cls.endpoint + '/' + app_id))

    @classmethod
    def delete(cls, app_id):
        """Delete a app with the given app ID."""
        return Requester.delete(cls.endpoint + '/' + app_id)
