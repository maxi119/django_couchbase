#!/usr/bin/env python

from setuptools import setup

setup(
      name="django-couchbase",
      version= '0.0.13',
      description="couchbase client for django memcache",
      long_description=open("README").read(),
      author="MaxiL",
      author_email="maxil@interserv.com.tw",
      maintainer="MaxiL",
      maintainer_email="maxil@interserv.com.tw",
      url="",
      download_url="https://github.com/maxi119/django_couchbase",
      packages=["django_couchbase"],
      install_requires=[
      	'couchbase',
      	'urllib3'
      ],
      classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

