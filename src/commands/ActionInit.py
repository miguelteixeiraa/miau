import argparse
from os import path, listdir, chdir, curdir


class ActionInit(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, **kwargs)
        dir_path = path.dirname(path.realpath(__file__))
        print(dir_path)
        chdir(dir_path)
        print(curdir)
        chdir("../themes")

        themes = listdir()
        print(themes)
        if nargs is not None:
            print("")

    def __call__(self, parser, namespace, values, option_string=None):

        print("%r %r %r" % (namespace, values, option_string))

        setattr(namespace, self.dest, values)
