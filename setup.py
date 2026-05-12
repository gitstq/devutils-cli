#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevUtils-CLI Setup
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='devutils-cli',
    version='1.0.0',
    author='DevUtils Team',
    author_email='dev@devutils.dev',
    description='🛠️ A lightweight, zero-dependency Python CLI toolbox for developers',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/gitstq/devutils-cli',
    py_modules=['devutils'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'devutils=devutils:main',
        ],
    },
    keywords='developer tools cli utility json base64 password uuid hash timestamp url encoding',
    project_urls={
        'Bug Reports': 'https://github.com/gitstq/devutils-cli/issues',
        'Source': 'https://github.com/gitstq/devutils-cli',
    },
)
