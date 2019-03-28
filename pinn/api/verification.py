"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

import json

from .list import List
from ..requester import Requester


class Verification(object):
    """Methods to create, list, or retrieve verifications."""

    OBJECT_NAME = 'verification'
    endpoint = '/users/{}/verifications'

    def __init__(self, response):
        """Initialize a user model with an API response."""
        self.verification_id = response['verification_id']
        self.created_at = response['created_at']
        self.object = response['object']
        self.score = response['score']
        self.genuine = response['genuine']
        self.biometrics = response['biometrics']
        self.signing = response['signing']
        self.metadata = response['metadata']

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    def dump(self):
        """Dump the model to a dictionary, method matches to json.dump() behavior"""
        return {'verification_id': self.verification_id,
                'created_at': self.created_at,
                'object': self.object,
                'score': self.score,
                'genuine': self.genuine,
                'biometrics': self.biometrics,
                'signing': self.signing,
                'metadata': self.metadata}

    @classmethod
    def create(cls, user_id, palm=None, signing=None, metadata=None):
        """Verify a user's biometrics and/or signatures."""
        data = {}
        if palm:
            data['palm'] = palm
        if signing:
            data['signing'] = signing
        if metadata:
            data['metadata'] = metadata
        return Verification(Requester.post(cls.endpoint.format(user_id), data=data))

    @classmethod
    def list(cls, user_id=None, limit=None, starting_after=None):
        """List all verifications for a user."""
        if user_id:
            response = Requester.get(cls.endpoint.format(user_id),
                                     params={'limit': limit,
                                             'starting_after': starting_after})
        else:
            response = Requester.get('/verifications',
                                     params={'limit': limit,
                                             'starting_after': starting_after})
        return List(response, Verification, limit)

    @classmethod
    def retrieve(cls, user_id, verification_id):
        """Retrieve a specific verification for a given user."""
        return Verification(Requester.get(cls.endpoint.format(user_id) + '/' + verification_id))
