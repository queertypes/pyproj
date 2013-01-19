#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Import installation modules
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Import the module that would be installed
import pyproj

def test():
   os.system("py.test")


# If you want to register your package on PyPi, do this.
def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

# If the latest CLI arg is 'publish', upload it to PyPi
if sys.argv[-1] == "publish":
    publish()
    sys.exit()

elif sys.argv[-1] == "test":
    test()
    sys.exit()

# Needs any other PyPi modules? List them here.
required = [
  'colorama',
  'webob'
]

# Notice that the following section is
# all a single function invocation.
#
# The Python packaging system is really powerful.
setup(
    # What's the project name?
    name='pyproj',

    # What version is being installed?
    version=pyproj.__version__,

    # Short description of project
    description='The empty Python project',

    # Long description, usually loaded from README + HISTORY
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),

    # Primary author contact information. Must be strings.
    author='Alejandro Cabrera',
    author_email='cpp.cabrera@gmail.com',

    # Project development URL
    url='https://github.com/cabrera/pyproj',

    # Additional files to bring in with the project
    data_files=[
        'README.md',
        'HISTORY.md',
    ],

    # Packages that this project installs
    packages= [
        'pyproj',
    ],

    # Dependencies for this project
    install_requires=required,

    # License identifier for the project
    license='ISC',

    #  PyPi project classifiers
    classifiers=(
#       'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Terminals :: Terminal Emulators/X Terminals',
    ),
)
