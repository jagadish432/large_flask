import unittest
import sys
sys.path.append('..')
from db.db_functions import *
from utilities.file_operations import *
from app import app


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # self.app = app.test_client()
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_get_book_types_list(self):
        bookTypes = get_json_from_file("test_data/book_types.json", os.path.abspath(os.path.dirname(__file__)))
        bookTypes = bookTypes["bookTypes"]
        assert (bookTypes.sort() == get_book_types_list().sort())

    def test_get_book_types_and_charges(self):
        bookTypeCharges = get_json_from_file("test_data/book_type_charges.json", os.path.abspath(os.path.dirname(__file__)))
        assert(bookTypeCharges == get_book_types_and_charges())


if __name__ == '__main__':
    unittest.main()
