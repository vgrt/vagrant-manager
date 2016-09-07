# -*- coding: utf-8 -*-

vagrant = 'vagrant'


def up():
    return '{} up'.format(vagrant)


def ssh():
    return '{} ssh'.format(vagrant)


def suspend():
    return '{} suspend'.format(vagrant)


def status():
    return '{} status'.format(vagrant)


def halt():
    return '{} halt'.format(vagrant)


def destroy(force=False):
    options = ''

    if force:
        options += '--force'

    return '{} destroy {}'.format(vagrant, options)


def share(**kwargs):
    options = ''

    name = kwargs.get('name')

    if name:
        options += '--name {}'.format(name)

    if options != '':
        options = ' ' + options

    return '{} share{}'.format(vagrant, options)
