
#-*- coding: utf-8 -*-
"""
@author:Bengali.ai
"""
#------------------------------------------------------------
from __future__ import print_function
#------------------------------------------------------------
from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='indicparser',
  version='0.0.10',
  description='Grapheme Parser for indic languages',
  long_description=open('README.md',encoding="utf-8").read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/mnansary/indicparser',  
  author='Bengali.AI',
  author_email='research.bengaliai@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['grapheme','indic languages'], 
  packages=find_packages(),
  install_requires=[''] 
)