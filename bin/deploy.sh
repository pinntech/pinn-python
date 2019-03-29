#!/bin/bash
python setup.py test sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
