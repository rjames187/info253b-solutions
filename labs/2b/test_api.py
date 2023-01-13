import unittest

from api import set_item, get_item, remove_item

class TestAPI(unittest.TestCase):

    def test_set_item_exists(self):
        db = {}

        set_item(db, "testkey1", "testvalue1")
        self.assertIn( "testkey1", db)

    def test_set_item_value_set(self):
        db = {}

        set_item(db, "testkey1", "testvalue1")
        self.assertEqual(db["testkey1"], "testvalue1")

    def test_get_item(self):

        db = {"testkey2": "testvalue2"}
        self.assertEqual(get_item(db, "testkey2"), "testvalue2")

    
    def test_remove_item(self):
        db = {"testkey2": "testvalue2"}
        remove_item(db, "testkey2")
        self.assertNotIn("testkey2", db)


if __name__ == '__main__':
    unittest.main()