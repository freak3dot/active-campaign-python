#!/bin/env python

import os
from setuptools import setup, find_packages

name = 'ActiveCampaign'
version = '0.1'
release = '1'
versrel = version + '-' + release
readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = file(readme).read()

setup(
    name = name,
    version = versrel,
    description = 'ActiveCampaign API client.',
    long_description = long_description,
    author = 'adulmec',
    author_email = 'info@activecampaign.com',
    maintainer = 'Ryan Johnston',
    maintainer_email = 'rjohnston@smartfile.com',
    url = 'http://github.com/rjohnston/active-campaign-python/',
    license = 'MIT',
    requires = [],
    packages=find_packages(),
    classifiers = (
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    zip_safe=False,
)
