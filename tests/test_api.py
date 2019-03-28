"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""


def test_import():
    import pinn


def test_configuration_error():
    import pinn
    try:
        pinn.User.create()
    except pinn.errors.ConfigurationError:
        pass
