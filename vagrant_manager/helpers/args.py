# -*- coding: utf-8 -*-

import sys


run_args = sys.argv[1:]


def has_args():
    return len(run_args) > 0


def get_arg(index):
    array_length = len(run_args)

    if array_length == 0:
        return None

    if array_length > 0 and array_length <= index:
        return None

    return run_args[index]


def has_arg(index):
    return run_args.get_arg(index) is not None


def is_unit_test():
    if not has_args():
        return False

    if '--unittest' in run_args:
        return True

    return False


def get_main_arg():
    return get_arg(0)


def is_start():
    return get_main_arg() == 'start'


def is_pause():
    return get_main_arg() == 'pause'


def is_stop():
    return get_main_arg() == 'stop'


def is_restart():
    return get_main_arg() == 'restart'


def is_status():
    return get_main_arg() == 'status'


def is_login():
    return get_main_arg() == 'login'


def is_delete():
    return get_main_arg() == 'delete'


def is_reinstall():
    return get_main_arg() == 'reinstall'


def is_share():
    return get_main_arg() == 'share'
