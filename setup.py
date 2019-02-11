#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests>=2.21.0', 'xmltodict>=0.11.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'pytest-raises', ]

setup(
    author="Jackson Maxfield Brown",
    author_email='jmaxfieldbrown@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python wrapper around the Washington State Legislative Web Services API with some extras.",
    entry_points={
        'console_scripts': [
            'my_example=pywslegislature.bin.my_example:main'
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pywslegislature',
    name='pywslegislature',
    packages=find_packages(include=['pywslegislature']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/JacksonMaxfield/pywslegislature',
    version='0.1.0',
    zip_safe=False,
)
