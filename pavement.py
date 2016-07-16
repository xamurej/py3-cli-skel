#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from paver.easy import options, Bunch
import paver.doctools
from paver.setuputils import setup, find_packages


def requirements():
    with open('requirements.txt') as handle:
        return handle.read().splitlines()


setup(
    name='CLIapp',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    entry_points={'console_scripts': ['cliapp=cli_app.cli:main'], },
    package_data={
        '': [
            'pavement.py',
            'setup.py',

        ],
    },
    data_files=[('', ['README.rst', 'requirements.txt'])],
    install_requires=requirements(),
    zip_safe=True,

    # Metadata for PyPI upload
    description='CLI example application',
    author='Your Name',
    author_email='you@example.com',
    url='https://github.com/xamurej/py3-cli-skel',
    # The complete list of classifiers can be checked at
    # <https://pypi.python.org/pypi?%3Aaction=list_classifiers>
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ], )

options(
    sphinx=Bunch(
        builddir="_build"
    )
)
