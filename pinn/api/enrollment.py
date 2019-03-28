"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

from ..requester import Requester


class Enrollment(object):
    """Methods to create, list, retrieve, or delete enrollments."""

    OBJECT_NAME = 'enrollment'
    endpoint = '/users/{}/enrollments'

    @classmethod
    def create(cls, user_id, palm=None):
        """Enroll biometrics to the user."""
        data = {}
        if palm:
            data['palm'] = palm
        return Requester.post(cls.endpoint.format(user_id), data=data)

    @classmethod
    def list(cls, user_id):
        """List all enrollments for a user."""
        return Requester.get(cls.endpoint.format(user_id))

    @classmethod
    def retrieve(cls, user_id, enrollment_id):
        """Retrieve a specific enrollment for a given user."""
        return Requester.get(cls.endpoint.format(user_id) + '/' + enrollment_id)

    @classmethod
    def delete(cls, user_id, enrollment_id):
        """Delete an enrollment for the user."""
        return Requester.delete(cls.endpoint.format(user_id) + '/' + enrollment_id)
