# -*- coding: utf-8 -*-

import shlex
import subprocess
import collections


def exec_command(command, **kwargs):
    shell = kwargs.get('shell', False)
    stdin = kwargs.get('stdin', None)
    stdout = kwargs.get('stdout', None)
    stderr = kwargs.get('stderr', None)

    kwargs.update(shell=shell)
    kwargs.update(stdin=stdin)
    kwargs.update(stdout=stdout)
    kwargs.update(stderr=stderr)

    if not isinstance(command, list):
        command = shlex.split(command)

    return subprocess.call(command, **kwargs)


def observe_command(command, **kwargs):
    shell = kwargs.get('shell', False)
    stdin = kwargs.get('stdin', subprocess.PIPE)
    stdout = kwargs.get('stdout', subprocess.PIPE)
    stderr = kwargs.get('stderr', subprocess.PIPE)

    kwargs.update(shell=shell)
    kwargs.update(stdin=stdin)
    kwargs.update(stdout=stdout)
    kwargs.update(stderr=stderr)

    if not isinstance(command, list):
        command = shlex.split(command)

    proc = subprocess.Popen(command, **kwargs)

    try:
        _stdin = proc.stdin.read()
    except IOError:
        _stdin = None

    try:
        _stdout = proc.stdout.read()
    except IOError:
        _stdout = None

    try:
        _stderr = proc.stderr.read()
    except IOError:
        _stderr = None

    if not _stdin:
        _stdin = None

    if not _stdout:
        _stdout = None

    if not _stderr:
        _stderr = None

    Result = collections.namedtuple('result', 'stdin, stdout, stderr')

    return Result(stdin=_stdin, stdout=_stdout, stderr=_stderr)


def create_kwargs(**kwargs):
    return kwargs
