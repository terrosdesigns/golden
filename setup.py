#!/bin/python3.4
# -*- coding: utf-8 -*-
"""
Terros 2019 -- https://terrosdesigns.com
"""

import sys
import os


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


packages = [
    'golden',
]


# if sys.argv[-1] == 'publish':
#     # PYPI now uses twine for package management.
#     # For this to work you must first `$ pip3 install twine`
#     os.system('python3 setup.py sdist bdist_wheel')
#     os.system('twine upload dist/*')
#     sys.exit()


# if sys.version_info[0] == 2 and sys.argv[-1] not in ['publish', 'upload']:
#     sys.exit('WARNING! You are attempting to install golden\'s '
#              'python3 repository on python2. PLEASE RUN '
#              '`$ pip3 install golden_data` for python3 or '
#              '`$ pip install golden_data` for python2')


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='golden',
    version='0.1.0',
    description='Python library to extract data from tech companies and topics.',
    long_description=long_description,
    author='Terros',
    author_email='terrosdesigns@gmail.com',
    url='https://github.com/terrosdesigns/golden/',
    packages=packages,
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
