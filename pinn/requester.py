"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import requests
from . import __title__
from ._version import get_versions
__version__ = get_versions()['version']
from .errors import PinnError, ConfigurationError


class Requester(object):
    """
    The requester class is a lightweight wrapper over python requests library.

    This class handles the request formation and response handling when interacting with
    the Pinn REST interface. It is leveraged to inject HTTP headers, handle errors and
    return JSON data.
    """

    @classmethod
    def post(cls, endpoint, data=None, params=None):
        """Performs a POST request to the given endpoint."""
        url = cls.url(endpoint)
        response = requests.post(url, json=data, params=params, headers=cls.headers())
        return cls.handle_response(response)

    @classmethod
    def get(cls, endpoint, params=None):
        """Performs a GET request to the given endpoint."""
        url = cls.url(endpoint)
        response = requests.get(url, params=params, headers=cls.headers())
        return cls.handle_response(response)

    @classmethod
    def patch(cls, endpoint, data=None, params=None):
        """Performs a PATCH request to the given endpoint."""
        url = cls.url(endpoint)
        response = requests.patch(url, json=data, params=params, headers=cls.headers())
        return cls.handle_response(response)

    @classmethod
    def delete(cls, endpoint, data=None, params=None):
        """Performs a DELETE request to the given endpoint."""
        url = cls.url(endpoint)
        response = requests.delete(url, json=data, params=params, headers=cls.headers())
        return cls.handle_response(response)

    @staticmethod
    def handle_response(response):
        """
        Handle the response of the request.

        Returns the JSON data if the request succeeded and has content. If the
        request succeeded but has no JSON content True is returned. Finally
        this method will raise a PinnError if an exception is encountered.
        """
        if response.status_code in [requests.codes.created,
                                    requests.codes.accepted,
                                    requests.codes.no_content]:
            return True
        elif response.status_code == requests.codes.ok:
            return response.json()
        else:
            raise PinnError.from_response(response)

    @staticmethod
    def headers():
        """
        Return the request headers to be sent with each request.

        Verifies before requesting that a Pinn secret key has been set.
        """
        from . import secret_key, api_version
        if secret_key is None:
            raise ConfigurationError('Pinn secret key has not been set, unable to perform requests')
        user_agent = "{}-{}".format(__title__, __version__)
        headers = {'Authorization': 'Bearer ' + secret_key,
                   'User-Agent': user_agent}
        if api_version:
            headers['Pinn-Version'] = api_version
        return headers

    @staticmethod
    def url(endpoint):
        """Return the fully qualified URL based off the api_host value and endpoint"""
        from . import api_host
        return api_host + endpoint
