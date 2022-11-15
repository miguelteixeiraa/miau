import argparse
from os import listdir


class ActionInit(argparse.Action):
    """
    test
    """

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, **kwargs)

        themes = listdir()
        print(themes)
        if nargs is not None:
            print("")

    def __call__(self, parser, namespace, values, option_string=None):

        setattr(namespace, self.dest, values)
