"""Utilities to initialize/setup configurations.

Typical usage example:

  themes = get_themes() # to get available themes
"""

from functools import reduce
from os import chdir, listdir, path
from typing import Callable


def get_themes() -> dict[str, str]:
    """Gets all available Miau themes

    Args:
      no-args

    Returns:
      a list containing all available themes separated by key (name of the theme)
      and value (address of the json file containing the theme).
    """

    dir_path = path.dirname(path.realpath(__file__))
    chdir(dir_path)
    chdir("../themes")

    themes: list[str] = listdir()

    get_tname: Callable[[str], str] = lambda file_name: file_name[
        0 : file_name.find(".json")
    ]

    map_themes: Callable[[dict[str, str], str], dict[str, str]] = (
        lambda acc, curr: acc.update({get_tname(curr): curr}) or acc
    )

    return reduce(map_themes, themes, {})
