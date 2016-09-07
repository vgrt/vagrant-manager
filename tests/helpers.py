#!/usr/bin/env python

from vagrant_manager.helpers import util


def run_as_unit_test(command):
    result = util.observe_command(['python -m vagrant_manager {} --unittest'.format(command)], shell=True)

    if result.stdout is None:
        return ''

    return result.stdout
