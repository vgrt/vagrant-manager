#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .helpers import args
from .helpers import command
from .helpers import util


if args.has_args():
    kwa = util.create_kwargs(unittest=args.is_unit_test())

    if args.is_start():
        command.run_command(command.start(), **kwa)

    elif args.is_pause():
        command.run_command(command.pause(), **kwa)

    elif args.is_stop():
        command.run_command(command.stop(), **kwa)

    elif args.is_restart():
        command.run_command(command.restart(), **kwa)

    elif args.is_status():
        command.run_command(command.status(), **kwa)

    elif args.is_login():
        command.run_command(command.login(), **kwa)

    elif args.is_delete():
        command.run_command(command.delete(), **kwa)

    elif args.is_reinstall():
        command.run_command(command.reinstall(), **kwa)

    elif args.is_share():
        # TODO: implement subarg processing (e.g.: name='sharename')
        share_args = util.create_kwargs()

        command.run_command(command.share(**share_args), **kwa)

else:
    # TODO: print usage
    pass
