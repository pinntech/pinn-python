"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from ..requester import Requester
from .list import List


class Event(object):
    """Event resource and interface.

    Attributes:
        response (dict): Underlying dictionary response
        object (str): Identifier for the resource
        event_id (str): Unique ID for the event
        created_at (int): Unix timestamp in seconds for when the app was created
        data (dict): Underlying data for the event
        request (str): ID of the request this event corresponds to
        event_type (str): The type of the event that occured
        livemode (bool): True if the event occured outside of sandbox environment
    """

    OBJECT_NAME = 'event'
    endpoint = '/v1/events'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.response = response
        self.object = response['object']
        self.event_id = response['event_id']
        self.created_at = response['created_at']
        self.data = response['data']
        self.request = response['request']
        self.event_type = response['type']
        self.livemode = response['livemode']

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn logs."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, Event, limit)

    @classmethod
    def retrieve(cls, event_id):
        """Retrieve an event with a provided event ID."""
        return Event(Requester.get(cls.endpoint + '/' + event_id))
