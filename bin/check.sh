#!/bin/bash
python3 setup.py test
twine check dist/*
