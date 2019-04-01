"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import json
from ..requester import Requester
from .list import List


class App(object):
    """App resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        app_id (str): Unique ID for the app
        created_at (int): Unix timestamp in seconds for when the app was created
        updated_at (int): Unix timestamp in seconds for when the app was last updated
        publishable_key (str): Non-secret key that is embedded to configure the SDK
        app_type (str): Either `ios`, `android` or `web`
        name (str): Name of the app
        description (str): Optional app description text
    """

    OBJECT_NAME = 'app'
    endpoint = '/v1/apps'

    def __init__(self, response):
        """Initialize a app model with an API response."""
        self.response = response
        self.object = response['object']
        self.app_id = response['app_id']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.publishable_key = response['publishable_key']
        self.app_type = response['app_type']
        self.name = response['name']
        self.description = response['description']

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
        """Create a new Pinn iOS/Android/Web app.

        Args:
            app_type (str): Either `ios`, `android` or `web`
            name (str): Human readable name for the app
            description (str, optional): Descriptive text for the app

        Returns:
            App: Newly created app resource

        Raises:
            pinn.errors.APIError: Internal server error
            pinn.errors.APIConnectionError: API is unreachable [501-503]
        """
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
        """Retrieve a Pinn iOS/Android/Web app.

        Args:
            app_id (str): ID of the app to query.

        Returns:
            App: The queried app resource

        Raises:
            pinn.errors.RequestFailedError: App not found
            pinn.errors.APIError: Internal server error
            pinn.errors.APIConnectionError: API is unreachable [501-503]
        """
        return App(Requester.get(cls.endpoint + '/' + app_id))

    @classmethod
    def delete(cls, app_id):
        """Delete a Pinn iOS/Android/Web app.

        Note:
            This may break your integration if app is currently in use live.

        Args:
            app_id (str): ID of the app to delete.

        Returns:
            Deleted: A deleted response

        Raises:
            pinn.errors.RequestFailedError: App not found
            pinn.errors.APIError: Internal server error
            pinn.errors.APIConnectionError: API is unreachable [501-503]
        """
        return Requester.delete(cls.endpoint + '/' + app_id)
