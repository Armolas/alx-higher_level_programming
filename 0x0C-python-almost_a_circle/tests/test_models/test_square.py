#!/usr/bin/python3


import unittest
import io
from unittest.mock import patch
"""imports the patch method"""


from models.square import Square
"""imports the square class"""


class TestSquare(unittest.TestCase):
    """Test the square class and methods"""
    def test_no_pos_arg(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_width(self):
        s1 = Square(4)
        self.assertEqual(s1.width, 4)

    def test_width_setter(self):
        s1 = Square(4)
        s1.width = 8
        self.assertEqual(s1.width, 8)

    def test_width_None(self):
        with self.assertRaises(TypeError):
            s1 = Square(None)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            s1 = Square("string")

    def test_width_float(self):
        with self.assertRaises(TypeError):
            s1 = Square(4.5)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            s1 = Square(-4, 4)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            s1 = Square(0, 4)

    def test_width_tuple(self):
        with self.assertRaises(TypeError):
            s1 = Square((4, 5), 4)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            s1 = Square([1, 2], 4)

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            s1 = Square({"key": "value", "key2": "value2"}, 4)

    def test_width_complx(self):
        s1 = Square((4 + 4), 3)
        self.assertEqual(s1.width, 8)

    def test_x(self):
        s1 = Square(4, 2)
        self.assertEqual(s1.x, 2)

    def test_x_setter(self):
        s1 = Square(4, 2)
        s1.x = 8
        self.assertEqual(s1.x, 8)

    def test_x_not_passed(self):
        s1 = Square(4)
        self.assertEqual(s1.x, 0)

    def test_x_None(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, None)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, "string")

    def test_x_float(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4.5)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            s1 = Square(4, -4)

    def test_x_zero(self):
        s1 = Square(4, 0)
        self.assertEqual(s1.x, 0)

    def test_x_tuple(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, (4, 5))

    def test_x_list(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, [1, 2])

    def test_x_dict(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, {"key": "value", "key2": "value2"})

    def test_x_complx(self):
        s1 = Square(10, (4 + 4))
        self.assertEqual(s1.x, 8)

    def test_y(self):
        s1 = Square(4, 4, 2)
        self.assertEqual(s1.y, 2)

    def test_y_setter(self):
        s1 = Square(4, 2)
        s1.y = 8
        self.assertEqual(s1.y, 8)

    def test_y_not_passed(self):
        s1 = Square(4, 2)
        self.assertEqual(s1.y, 0)

    def test_y_None(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, None)

    def test_y_string(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, "string")

    def test_y_float(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, 4.5)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            s1 = Square(4, 4, -4)

    def test_y_zero(self):
        s1 = Square(4, 4, 0)
        self.assertEqual(s1.y, 0)

    def test_y_tuple(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, (4, 5))

    def test_y_list(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, [1, 2])

    def test_y_dict(self):
        with self.assertRaises(TypeError):
            s1 = Square(4, 4, {"key": "value", "key2": "value2"})

    def test_y_complx(self):
        s1 = Square(10, 4, (4 + 4))
        self.assertEqual(s1.y, 8)

    def test_with_id(self):
        s1 = Square(4, 2, id=20)
        self.assertEqual(s1.id, 20)

    def test_y_no_x(self):
        s1 = Square(4, y=5)
        self.assertEqual(s1.y, 5)

    def test_all_values_passes(self):
        s1 = Square(4, 2, 3, 7)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 7)

    def test_area(self):
        s1 = Square(4, 2)
        s2 = Square(3, 2, 2, 5)
        self.assertEqual(s1.area(), 16)
        self.assertEqual(s2.area(), 9)

    def test_area_with_args(self):
        s1 = Square(4, 3, 2, 3)
        with self.assertRaises(TypeError):
            s1.area('arg')

    def test_display(self):
        s1 = Square(2)
        s2 = Square(4, 0, 0, 5)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            expected = "##\n##\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            expected = "####\n####\n####\n####\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))

    def test_str(self):
        s1 = Square(4, 3, 3, 16)
        s2 = Square(10)
        s3 = Square(6, 5, 7)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(s1)
            expected = f"[Square] ({s1.id}) 3/3 - 4\n"
            self.assertEqual(mock_stdout.getvalue(), expected)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(s2)
            expected = f"[Square] ({s2.id}) 0/0 - 10\n"
            self.assertEqual(mock_stdout.getvalue(), expected)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(s3)
            expected = f"[Square] ({s3.id}) 5/7 - 6\n"
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display1(self):
        s1 = Square(2, 2, 2)
        s2 = Square(4, 0, 3, 5)
        s3 = Square(3, 3)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            expected = "\n\n  ##\n  ##\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            expected = "\n\n\n####\n####\n####\n####\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s3.display()
            expected = "   ###\n   ###\n   ###\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))

    def test_update(self):
        s1 = Square(4, id=6)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 6)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(3, 6)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.width, 6)
        s1.update(7, 8, 9)
        self.assertEqual(s1.id, 7)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.x, 9)
        s1.update(5, 4, 3, 2)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)

    def test_update_no_arg(self):
        s1 = Square(4, 2, id=4)
        s1.update()
        self.assertEqual(s1.id, 4)
