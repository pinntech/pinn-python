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
        except:  # NOQA FIXME
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
    """The Pinn host is unreachable, you can and should retry this request"""
    pass


PINN_ERROR_CODE_MAP = {
    requests.codes.internal_server_error: 'internal_server_error',  # 500
    requests.codes.service_unavailable: 'service_unavailable',      # 502
    requests.codes.gateway_timeout: 'gateway_timeout',              # 503
    requests.codes.bad_gateway: 'bad_gateway'                       # 504
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
    'internal_server_error': APIError,           # 500
    'service_unavailable': APIConnectionError,   # 502
    'bad_gateway': APIConnectionError,           # 503
    'gateway_timeout': APIConnectionError        # 504
}


# Non API Errors
# --------------
class IDTokenVerificationError(Exception):
    """This exception can be raised during an attempt to verify an ID token.

    Potentially this can be from:
        - An invalid JWT signature
        - Missing required claims
        - `amr` claim mismatch from expectations
    """
    pass


class ConfigurationError(Exception):
    """This error is thrown fast if the library is misconfigured.

    For example, if you attempt to call the library without a `secret_key` value
    set a ConfigurationError will be thrown.
    """
    pass
