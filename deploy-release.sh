#!/usr/bin/env sh

python setup.py sdist bdist_wheel upload && mkdocs gh-deploy
