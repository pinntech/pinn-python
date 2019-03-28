#!/bin/bash
python3 setup.py test
python3 setup.py build sdist bdist_egg upload
