# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 15:21:59 2015

@author: Administrator
"""
#%%
#from setuptools import find_packages, setup
#%%
#setup(name='setuptest',
#      version='1.0',
#      description='setuptest',
#      author='xmduhan',
#      author_email='xmduhan@gmail.com',
#      url='https://www.python.org/sigs/distutils-sig/',
#      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
#     )

from setuptools import setup, find_packages
setup(
    name = "setuptest",
    version = "0.1",
    packages = find_packages(),
    scripts = ['test.py','__init__.py'],
)