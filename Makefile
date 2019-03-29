.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo ""
	@echo "* dev        -   Install all deps for dev env"
	@echo "* docs       -   Create HTML documentation for project"
	@echo "* test       -   Run all tests with coverage"
	@echo "* lint       -   Runs code conformance tests"
	@echo "* deploy     -   Deploy package to production PyPi"
	@echo "* test-deply -   Deploy package to test PyPi"

clean:
	rm -rf dist/*

dev:
	pip install coverage
	pip install codecov
	pip install flake8
	pip install pylint
	pip install twine
	pip install sphinx
	pip install sphinx-autobuild
	pip install sphinx_rtd_theme
	pip install -e .

docs:
	$(MAKE) -C docs html

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	pytest
	make lint

lint:
	flake8 --config setup.cfg pinn

deploy:
	python setup.py test sdist bdist_wheel
	twine upload dist/*

test-deploy:
	python setup.py test sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
