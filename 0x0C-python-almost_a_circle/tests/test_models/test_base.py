import unittest
"""This imports the unittest module"""


from models.base import Base
"""This imports the base class"""


class TestBase(unittest.TestCase):
    """This is the class for the base tests"""
    def test_no_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_with_id(self):
        base1 = Base(12)
        base2 = Base(24)
        self.assertEqual(base1.id, 12)
        self.assertEqual(base2.id, 24)

    def test_with_string_id(self):
        base1 = Base('id_no')
        self.assertEqual(base1.id, 'id_no')
