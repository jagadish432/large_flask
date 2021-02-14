import unittest
import sys
sys.path.append('..')
from db.db import BookTypes


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bookType = BookTypes()

    def test_repr(self):
        self.bookType.type = 'fiction'
        self.bookType.charge = 3
        assert (repr(self.bookType) == "<Type: fiction Charge: 3>")


if __name__ == '__main__':
    unittest.main()
