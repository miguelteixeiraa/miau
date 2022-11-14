"""Test module for the Utils module"""
import unittest
from config.utils import get_themes


class UtilsTest(unittest.TestCase):
    """Test cases for the Utils module"""

    def test_get_themes(self) -> None:
        """
        get_names should return the available themes list
        """
        themes = get_themes()
        self.assertTrue("meow" in themes.keys())

    #


#


if __name__ == "__main__":
    unittest.main()
