#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2018 by Mitchell Lisle
:license: MIT, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

setup(name='napoleon',
      version='MysteriousGoanna',
      description='A python package for making Altair plots very simple',
      url='http://github.com/mitchelllisle/napoleon',
      author='Mitchell Lisle',
      author_email='lislemitchell@gmail.com',
      license='MIT',
      packages=['napoleon'],
      zip_safe=False,
      python_requires='>=3'
)
