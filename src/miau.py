import argparse
from commands.action_init import ActionInit

parser = argparse.ArgumentParser(
    prog="Miau",
    description="C++ Project Manager",
    epilog="The Manager for the rest of us",
)

parser.add_argument("init", action=ActionInit)
args = parser.parse_args()
