# -*- coding: utf-8 -*-
__author__ = 'kky'

from setuptools import setup, find_packages

# python3 setup.py sdist     # 生成pip支持的格式，下文以此为例
# sudo pip3 install -e PyTools/
setup(
    name='funnytools',
    version='0.0.1',
    description='this is a funny python3 tools',
    url='https://github.com/kkyflying/FunnyTools',
    author='kky',
    author_email='kkyflying@gmail.com',
    license='MIT',
    keywords='python3 tools',
    packages=find_packages(),
    platforms = 'linux mac',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ]
)

