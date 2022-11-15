"""Test module for the Utils module"""
import unittest
from config.utils import get_themes, get_miaurc


class UtilsTest(unittest.TestCase):
    """Test cases for the Utils module"""

    def test_get_themes(self) -> None:
        """
        get_names should return the available themes list
        """
        themes = get_themes()
        self.assertTrue("meow" in themes.keys())

    #

    def test_get_miaurc(self) -> None:
        """
        get_miaurc should return a dictionary with the .miaurc configurations
        """

        raises = False
        miaurc = None
        try:
            miaurc = get_miaurc()
        except FileNotFoundError:
            raises = True
        #

        self.assertFalse(raises)
        self.assertTrue(len(miaurc.keys()))

    #


#


if __name__ == "__main__":
    unittest.main()

#
