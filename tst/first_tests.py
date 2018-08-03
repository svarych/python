# import pytest
import unittest


class TestFirstOnBamboo(unittest.TestCase):
    def test0(self):
        self.assertTrue(1)

    def test1(self):
        self.assertFalse(0)

    def test2(self):
        self.assertEquals(1, "2")

# if __name__ == 'main':
#     unittest.main
