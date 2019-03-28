"""
setup.py for pinn-python
"""

__author__ = "Pinn Technologies, Inc."
__email__ = "developers@pinn.ai"
__copyright__ = "Copyright 2019, Pinn Technologies, Inc."

import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS = filter(None, open(
    os.path.join(this_dir, 'requirements', 'main.txt')).read().splitlines())

import versioneer

setup(
    name='pinn',
    author=__author__,
    author_email=__email__,
    license="MIT",
    url="https://pinn.readthedocs.org",
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=list(REQUIREMENTS),
    classifiers=[k for k in open('CLASSIFIERS').read().split('\n') if k],
    description='Python bindings for the Pinn REST API',
    long_description=open('README.rst').read() + open('HISTORY.rst').read(),
    packages=find_packages(exclude=["tests*"])
)
