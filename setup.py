#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='PyRogue',
      version='0.0.1',
      description='Roguelike written in python',
      author='Redacted',
      author_email='britt.mathis@gmail.com',
      license='GPL',
      url='https://bmuk.io/pyrogue',
      packages=['pyrogue', 'tests'],
      long_description=read('README.md')
      entry_points={
          'console_scripts': ['pyrogue=pyrogue:main']
      }
     )
