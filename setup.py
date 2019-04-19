#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests>=2.21.0',
    'xmltodict>=0.11.0',
]

setup_requirements = [
    'pytest-runner>=4.2',
]

test_requirements = [
    'pytest>=3.8.2',
    'pytest-cov>=2.6.1',
    'pytest-raises>=0.10',
]

dev_requirements = [
    'pip>=19.0.2',
    'ipython>=7.4.0',
    'bumpversion>=0.5.3',
    'wheel>=0.32.1',
    'flake8>=3.5.0',
    'tox>=3.5.2',
    'coverage>=4.5.1',
    'Sphinx>=1.8.1',
    'twine>=1.12.1',
    'pytest>=3.8.2',
    'pytest-cov>=2.6.1',
    'pytest-raises>=0.10',
    'pytest-runner>=4.2',
]

extra_requirements = {
    'test': test_requirements,
    'setup': setup_requirements,
    'dev': dev_requirements,
}

setup(
    author='Jackson Maxfield Brown',
    author_email='jmaxfieldbrown@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Python wrapper around the Washington State Legislative Web Services API with some extras.',
    entry_points={
        'console_scripts': [],
    },
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pywslegislature',
    name='pywslegislature',
    packages=find_packages(include=['pywslegislature']),
    python_requires='>=3.6',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url='https://github.com/JacksonMaxfield/pywslegislature',
    version='0.1.0',
    zip_safe=False,
)
