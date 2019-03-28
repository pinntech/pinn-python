"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

from ..requester import Requester
from .list import List


class WebhookEndpoint(object):
    """Methods to create, list, retrieve, update or delete users."""

    OBJECT_NAME = 'webhookendpoint'
    endpoint = '/v1/webhook_endpoints'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.webhook_endpoint_id = response['webhook_endpoint_id']
        self.created_at = response['created_at']
        self.updated_at = response['updated_at']
        self.status = response['status']
        self.url = response['url']
        self.events = response['events']
        self.livemode = response['livemode']
        self.secret = response['secret']
        self.object = response['object']

    @classmethod
    def create(cls, url, events):
        """Create Pinn webhook endpoint."""
        data = {'url': url,
                'events': events}
        return WebhookEndpoint(Requester.post(cls.endpoint, data=data))

    @classmethod
    def update(cls, webhook_endpoint_id, url=None, events=None, status=None):
        """Update Pinn webhook endpoint."""
        data = {}
        if url:
            data['url'] = url
        if events:
            data['events'] = events
        if status:
            data['status'] = status
        return WebhookEndpoint(Requester.patch(cls.endpoint + '/' + webhook_endpoint_id, data=data))

    @classmethod
    def list(cls, limit=None, starting_after=None):
        """List created Pinn logs."""
        response = Requester.get(cls.endpoint, params={'limit': limit,
                                                       'starting_after': starting_after})
        return List(response, WebhookEndpoint, limit)

    @classmethod
    def retrieve(cls, webhook_endpoint_id):
        """Retrieve an webhook_endpoint with a provided webhook_endpoint ID."""
        return WebhookEndpoint(Requester.get(cls.endpoint + '/' + webhook_endpoint_id))

    @classmethod
    def delete(cls, webhook_endpoint_id):
        """Delete a webhook_endpoint with a provided webhook_endpoint ID."""
        return Requester.delete(cls.endpoint + '/' + webhook_endpoint_id)
