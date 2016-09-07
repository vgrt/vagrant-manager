# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vagrant-manager',
    version='0.0.0',
    description='A manager for Vagrant for more intuitive and easy Vagrant usage.',
    long_description=readme,
    author='Richard King',
    author_email='richrdkng@gmail.com',
    url='https://github.com/vgrt/vagrant-manager',
    license=license,
    test_suite='tests',
    packages=find_packages(exclude=('docs', 'scripts', 'tests')),
)

