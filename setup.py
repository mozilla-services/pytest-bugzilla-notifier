#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-bugzilla-notifier',
    version='1.1.0',
    author='Chris Hartjes',
    author_email='chartjes@mozilla.com',
    maintainer='Chris Hartjes',
    maintainer_email='chartjes@mozilla.com',
    license='Mozilla Public License 2.0',
    url='https://github.com/mozilla-services/pytest-bugzilla-notifier',
    packages=['pytest_bugzilla_notifier'],
    package_dir={'pytest_bugzilla_notifier': 'pytest_bugzilla_notifier'},
    description='A plugin that allows you to post test runs to BugZilla tickets and create new tickets',
    long_description=read('README.rst'),
    install_requires=['pytest>=2.9.2', 'requests', 'ConfigObj'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',

    ],
    entry_points={
        'pytest11': [
            'pytest-bugzilla-notifier = pytest_bugzilla_notifier.conftest',
        ],
    },
)
