# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:18:17 2019

@author: jkcle
"""

from setuptools import setup

setup(name='chowtest',
      version=' 1.0',
      description='Package to test for structural breaks at a specified date.',
      url='https://github.com/jkclem/chowtest',
      author='John Clements',
      author_email='jkclements2016@gmail.com',
      license='MIT',
      packages=['chowtest'],
      install_requires=[
          'pandas', 'numpy', 'sklearn', 'scipy'
      ],
      zip_safe=False)