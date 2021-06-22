#!/usr/bin/env python3
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

"""
Entry point for dial ui.
"""

import sys

from typing import List
def main(sys_args: List = sys.argv[1:]):
    """
    Entry point for Dial. Initialize components and stars the application.

    Args:
        sys_args: A list of arguments from the command line.
    """
    try:
        import dial_core
        app_config = dial_core.utils.initialization.parse_args(sys_args)

        # Initialize
        from dial_gui.utils import initialization
        initialization.initialize(app_config)
    
        # Run
        from dial_gui import app
        sys.exit(app.run(app_config))
    except ModuleNotFoundError as ex:
        print("Module not found error. Error : {} \nTry running 'install.py' first".format(ex))
        sys.exit(0)
        # Parse arguments
    return


main()
