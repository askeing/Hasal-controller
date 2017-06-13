#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from setuptools import setup, find_packages

if 'win32' in sys.platform:
    DEFAULT_REQUIREMENT = "requirements-win.txt"
else:
    DEFAULT_REQUIREMENT = "requirements.txt"

with open(DEFAULT_REQUIREMENT) as f:
    deps = f.read().splitlines()

version = "0.1.0"

# main setup script
setup(
    name="Hasal-controller",
    version=version,
    description="The Celery Worker of Hasal Performance Framework.",
    author="Mozilla Taiwan",
    author_email="hasal-dev@mozilla.com",
    url='https://github.com/askeing/Hasal-controller',
    license="MPL",
    install_requires=deps,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
