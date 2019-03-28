"""
:copyright: (c) 2019 Pinn Technologies, Inc.
:license: MIT
"""

import io
from setuptools import setup, find_packages
import versioneer

with io.open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='pinn',
    author='Pinn Technologies, Inc.',
    author_email='developers@pinn.ai',
    license="MIT",
    url="https://github.com/pinntech/pinn-python",
    zip_safe=False,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    install_requires=[
        'requests >= 2.20; python_version >= "3.0"',
        'requests[security] >= 2.20; python_version < "3.0"',
        'pyjwt >= 1.7.1',
    ],
    tests_require=[
        "pytest >= 3.4",
        "pytest-mock >= 1.7",
        "pytest-xdist >= 1.22",
        "pytest-cov >= 2.5",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    project_urls={
        "Bug Tracker": "https://github.com/pinntech/pinn-python/issues",
        "Documentation": "https://pinn.readthedocs.org",
        "Source Code": "https://github.com/pinntech/pinn-python",
    },
    keywords='pinn api client library authentication',
    classifiers=[k for k in open('CLASSIFIERS').read().split('\n') if k],
    description='Python bindings for the Pinn REST API',
    long_description=readme,
    packages=find_packages(exclude=["tests*"])
)
