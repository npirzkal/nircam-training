#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
    name='nircam-training',
    version = '0.1',
    description = 'Training repository for NIRCam branch',
    long_description = ('A space for NIRCam branch members to practice'
                        'using workflows and commands on GitHub for'
                        'code collaboration.'),
    author = 'STScI NIRCam Team',
    author_email = 'acanipe@stsci.edu',
    keywords = ['astronomy'],
    classifiers = ['Programming Language :: Python'],
    packages = find_packages(exclude=["examples"]),
    install_requires = [],
    include_package_data = True
)
