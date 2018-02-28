# -*- coding: utf-8 -*-
__author__ = 'kky'

from setuptools import setup, find_packages



setup(
    name='pytools',
    version='0.0.1',
    description='a python3 tools lib',
    url='',
    author='kky',
    author_email='kkyflying@gmail.com',
    license='MIT',
    keywords='tools',
    packages=find_packages('src'),
    python_requires='>=3',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ],
)