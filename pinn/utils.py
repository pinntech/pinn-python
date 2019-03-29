"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import jwt
from .errors import IDTokenVerificationError


class IDToken(object):
    """Provides functionality for verifying an incoming Pinn ID token."""

    @staticmethod
    def verify(id_token, amr):
        """
        Validates the signature and ensures all amr values are present in the token.

        If successful, a pinn.User object is returned.
        """
        from . import secret_key, api_host
        if secret_key is None:
            raise ValueError('Pinn `secret_key` has not been set')
        try:
            claims = jwt.decode(id_token, key=secret_key)
        except Exception as e:
            raise IDTokenVerificationError(str(e))
        if 'sub' not in claims:
            raise IDTokenVerificationError('`sub` claim not provided in JWT')
        if 'amr' not in claims:
            raise IDTokenVerificationError('`amr` claim not provided in JWT')
        if 'iss' not in claims:
            raise IDTokenVerificationError('`iss` claim not provided in JWT')
        if claims['iss'] != api_host:
            raise IDTokenVerificationError(
                '`iss` claim provided was {} and was expected to be {}'.format(claims['iss'], api_host))
        if not set(amr).issubset(set(claims['amr'])):
            raise IDTokenVerificationError('`amr` was invalid and did not contain all methods required. Requested: {}, Received: {}'.format(amr, claims['amr']))
        return claims


class WebhookSignature(object):
    pass
