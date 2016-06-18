#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import paver.doctools

from paver.easy import *
from paver.setuputils import setup, find_packages

setup(name='CLI example application',
      version='1.0',
      description='CLI example application',
      author='Your Name',
      author_email='you@example.com',
      url='http://download.example.com/cli_app',
      entry_points={
           'console_scripts': ['cliapp=cli_app.cli:main'],
      },
      packages=find_packages(exclude=['tests', 'venv', 'docs']),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Topic :: Utilities',
      ],
      zip_safe=True,
      )
