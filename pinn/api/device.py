"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from .list import List
from .log import Log
from ..requester import Requester


class Device(object):
    """Device resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        device_id (str): Unique ID for the device
        user_id (str): ID of the user the device is registered to
        created_at (int): Unix timestamp in seconds for when the app was created
        updated_at (int): Unix timestamp in seconds for when the app was last updated
        name (str): Human readable name of the device
        make (str): Manufacturer make of the device
        model (str): Model identifier of the device
        platform (str): Either `ios` or `android`
        platform_version (str): Last recorded platform version of the device
        framework_version (str): Last recorded framework version for the device
        push_notification_token (str, optional): Device APNS or FCM push notification token
    """

    OBJECT_NAME = 'key'
    endpoint = '/v1/devices'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.response = response
        self.object = response['object']
        self.device_id = response['device_id']
        self.user_id = response['user_id']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.name = response['name']
        self.make = response['make']
        self.model = response['model']
        self.platform = response['platform']
        self.platform_version = response['platform_version']
        self.framework_version = response['framework_version']
        self.push_notification_token = response.get('push_notification_token')

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn users."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, Device, limit)

    @classmethod
    def list_logs(cls, device_id, limit=None, starting_after=None):
        """List created Pinn users."""
        endpoint = cls.endpoint + '/' + device_id + '/logs'
        response = Requester.get(endpoint, params={'limit': limit,
                                                   'starting_after': starting_after})
        return List(response, Log, limit)

    @classmethod
    def retrieve(cls, device_id):
        """Retrieve a specific key for a given user."""
        return Device(Requester.get(cls.endpoint + '/' + device_id))

    @classmethod
    def delete(cls, device_id):
        """Remove a key from the user's keychain."""
        return Requester.delete(cls.endpoint + '/' + device_id)
