.PHONY: clean clean-test clean-pyc clean-build copy-cookie format-python help
.DEFAULT_GOAL := help

help:
	@echo "clean 			remove all build, test, coverage and Python artifacts"
	@echo "clean-build 		remove build artifacts"
	@echo "clean-pyc		remove Python file artifacts"
	@echo "clean-test		remove test and coverage artifacts"
	@echo "copy-cookie		copies the cookiecutter-git features into the to-be generated project dir"
	@echo "format-python	formats the python source files using the uncompromising black."
	@echo "test 			run tests quickly with the default Python"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -frv build/
	rm -frv dist/
	rm -frv .eggs/
	find . -name '*.egg-info' -exec rm -frv {} +
	find . -name '*.egg' -exec rm -frv {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -frv {} +
	find . -name '*.pyo' -exec rm -frv {} +
	find . -name '*~' -exec rm -frv {} +
	find . -name '__pycache__' -exec rm -frv {} +

clean-test:
	rm -frv .tox/
	rm -fv .coverage
	rm -frv htmlcov/
	rm -frv .pytest_cache

def copy-cookie:
	cp -afrv cookiecutter.json '{{cookiecutter.repo_slug}}'
	cp -afrv hooks '{{cookiecutter.repo_slug}}'
	cp -afrv '{{cookiecutter.repo_slug}}' '{{cookiecutter.repo_slug}}'

def format-python:
	black --line-length 79 {{cookiecutter.repo_slug}}
	flake8 {{cookiecutter.repo_slug}} tests
	git add --all

test:
	pytest --capture=no --cov-report term:skip-covered --cov-report html --cov=. tests
