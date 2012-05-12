#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(name='python-twitpic',
    description='DjangoVideoThumbs',
    author='Chris McMichael',
    author_email='macmichael01@gmail.com',
    url="https://github.com/macmichael01/django-videothumbs",
    version='0.91',
    packages = find_packages(),
    long_description="DjangoVideoThumbs - Videos need thumbnails too",
    keywords="Django Video thumbnails",
    license="BSD"
)