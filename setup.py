# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE.txt for details)
# https://github.com/mysmarthub/sfd/
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
from os.path import join, dirname

from sfd import settings

PACKAGE = settings.PACKAGE
VERSION = settings.VERSION
AUTHOR = settings.AUTHOR
AUTHOR_EMAIL = settings.EMAIL
DESCRIPTION = settings.DESCRIPTION
NAME = settings.NAME
URL = settings.URL
LICENSE = settings.LICENSE
LONG_DESCRIPTION = open(join(dirname(__file__), 'README.md')).read()
INSTALL_REQUIRES = open(join(dirname(__file__), 'requirements.txt')).read()
PLATFORM = settings.PLATFORM
CLASSIFIERS = settings.CLASSIFIERS
KEYWORDS = settings.KEYWORDS
setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    version=VERSION,
    license=LICENSE,
    platforms=PLATFORM,
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
    keywords=KEYWORDS,
    entry_points={
        'console_scripts':
            ['sfd = sfd.sfd:cli']
        }
)
