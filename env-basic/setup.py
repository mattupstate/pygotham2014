# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~
"""

import sys

from setuptools import setup, find_packages

setup(
    name='MyApp',
    version='0.1.0',
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'pytest']
)
