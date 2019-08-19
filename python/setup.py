# coding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import sys
from distutils.core import setup, Command
from shutil import rmtree

from setuptools import find_packages  # , setup, Command

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

PROJECT_NAME = "simple_calls"

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()
about = {}
with open(os.path.join(here, PROJECT_NAME, "_version.py")) as f:
    exec(f.read(), about)
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()
required = [
    'requests'
]



setup(
    name=PROJECT_NAME,
    version=about['__version__'],
    description='Json Katas',
    long_description=long_description,
    # markdown is not supported. Easier to just convert md to rst with pandoc
    # long_description_content_type='text/markdown',
    author='Matthew Martin',
    author_email='matthewdeanmartin@gmail.com',
    url='https://github.com/matthewdeanmartin/' + PROJECT_NAME,
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'run_calls=simple_calls.main:run',
        ]
    },
    install_requires=required,
    extras_require={},
    include_package_data=True,
    license='MIT',
    keywords="kata",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    # cmdclass={'upload': UploadCommand, },
    # setup_cfg=True,
    setup_requires=[],

)