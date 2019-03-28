"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import requests


class PinnError(Exception):
    """Base exception class for a Pinn API Error."""

    def __init__(self, response):
        try:
            error = response.json()['error']
            self._message = error["message"]
            self.code = error["code"]
            self.type = error["type"]
        except:
            self._message = response.reason
            self.code = response.status_code
            self.type = PINN_ERROR_CODE_MAP[response.status_code]
        super(PinnError, self).__init__(self._message)

    @staticmethod
    def from_response(response):
        """Create an error of the right class from an API response."""
        if response.status_code == requests.codes.internal_server_error:
            return APIError(response)
        if response.status_code in [requests.codes.bad_gateway,
                                    requests.codes.service_unavailable,
                                    requests.codes.gateway_timeout]:
            return APIConnectionError(response)
        error = response.json()["error"]
        cls = PINN_ERROR_TYPE_MAP.get(error['type'], PinnError)
        return cls(response)


class InvalidRequestError(PinnError):
    pass


class AuthenticationError(PinnError):
    pass


class RequestFailedError(PinnError):
    pass


class PermissionError(PinnError):
    pass


class RateLimitError(PinnError):
    pass


class APIError(PinnError):
    pass


class APIConnectionError(PinnError):
    pass


class SignatureVerificationError(PinnError):
    pass


PINN_ERROR_CODE_MAP = {
    requests.codes.internal_server_error: 'internal_server_error',
    requests.codes.bad_gateway: 'bad_gateway',
    requests.codes.service_unavailable: 'service_unavailable',
    requests.codes.gateway_timeout: 'gateway_timeout'
}

PINN_ERROR_TYPE_MAP = {
    'bad_request': InvalidRequestError,          # 400
    'unauthorized': AuthenticationError,         # 401
    'forbidden': AuthenticationError,            # 403
    'not_found': InvalidRequestError,            # 404
    'method_not_allowed': InvalidRequestError,   # 405
    'conflict': RequestFailedError,              # 409
    'unprocessable_entity': RequestFailedError,  # 422
    'rate_limit_exceeded': RateLimitError,       # 429
    'internal_server_error': APIError            # 500
}


# Non API Errors
# --------------
class IDTokenVerificationError(Exception):
    pass


class ConfigurationError(Exception):
    pass
