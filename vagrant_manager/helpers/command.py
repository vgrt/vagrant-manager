# -*- coding: utf-8 -*-

from __future__ import print_function
import vagrant
import util


def run_command(command, **kwargs):
    is_unit_test = kwargs.get('unittest', False)

    if is_unit_test:
        print(command, end='')
        return

    util.exec_command([command], shell=True)


def start():
    return '{} && {}'.format(vagrant.up(), vagrant.ssh())


def pause():
    return vagrant.suspend()


def stop():
    return vagrant.halt()


def restart():
    return '{} && {} && {}'.format(vagrant.halt(), vagrant.up(), vagrant.ssh())


def status():
    return vagrant.status()


def login():
    return vagrant.ssh()


def delete():
    return vagrant.destroy(True)


def reinstall():
    return '{} && {} && {}'.format(vagrant.destroy(True), vagrant.up(), vagrant.ssh())


def share(**kwargs):
    return vagrant.share(**kwargs)
