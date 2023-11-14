import unittest
import io
from unittest.mock import patch
"""imports the patch method"""


from models.rectangle import Rectangle
"""imports the rectangle module"""


class TestRectangle(unittest.TestCase):
    """Test the rectangle class and methods"""
    def test_one_pos_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4)

    def test_no_pos_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_width(self):
        rect1 = Rectangle(4, 2)
        self.assertEqual(rect1.width, 4)

    def test_width_setter(self):
        r1 = Rectangle(4, 2)
        r1.width = 8
        self.assertEqual(r1.width, 8)

    def test_width_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 4)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("string", 4)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4.5, 4)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-4, 4)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 4)

    def test_width_tuple(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle((4, 5), 4)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 2], 4)

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle({"key": "value", "key2": "value2"}, 4)

    def test_width_complx(self):
        r1 = Rectangle((4 + 4), 3)
        self.assertEqual(r1.width, 8)

    def test_height(self):
        rect1 = Rectangle(4, 2)
        self.assertEqual(rect1.height, 2)

    def test_height_setter(self):
        r1 = Rectangle(4, 2)
        r1.height = 8
        self.assertEqual(r1.height, 8)

    def test_height_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, None)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, "string")

    def test_height_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 4.5)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, -4)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 0)

    def test_height_tuple(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, (4, 5))

    def test_height_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, [1, 2])

    def test_height_dict(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, {"key": "value", "key2": "value2"})

    def test_height_complx(self):
        r1 = Rectangle(10, (4 + 4))
        self.assertEqual(r1.height, 8)

    def test_x(self):
        rect1 = Rectangle(4, 2, 2)
        self.assertEqual(rect1.x, 2)

    def test_x_setter(self):
        r1 = Rectangle(4, 2)
        r1.x = 8
        self.assertEqual(r1.x, 8)

    def test_x_not_passed(self):
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.x, 0)

    def test_x_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, None)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, "string")

    def test_x_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4.5)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 2, -4)

    def test_x_zero(self):
        r1 = Rectangle(4, 2, 0)
        self.assertEqual(r1.x, 0)

    def test_x_tuple(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, (4, 5))

    def test_x_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, [1, 2])

    def test_x_dict(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, {"key": "value", "key2": "value2"})

    def test_x_complx(self):
        r1 = Rectangle(10, 4, (4 + 4))
        self.assertEqual(r1.x, 8)

    def test_x(self):
        rect1 = Rectangle(4, 2, 4, 2)
        self.assertEqual(rect1.y, 2)

    def test_y_setter(self):
        r1 = Rectangle(4, 2)
        r1.y = 8
        self.assertEqual(r1.y, 8)

    def test_y_not_passed(self):
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.y, 0)

    def test_y_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, None)

    def test_y_string(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, "string")

    def test_y_float(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, 4.5)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 2, 4, -4)

    def test_y_zero(self):
        r1 = Rectangle(4, 2, 4, 0)
        self.assertEqual(r1.y, 0)

    def test_y_tuple(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, (4, 5))

    def test_y_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, [1, 2])

    def test_y_dict(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 2, 4, {"key": "value", "key2": "value2"})

    def test_y_complx(self):
        r1 = Rectangle(10, 4, 4, (4 + 4))
        self.assertEqual(r1.y, 8)

    def test_with_id(self):
        r1 = Rectangle(4, 2, id=20)
        self.assertEqual(r1.id, 20)

    def test_y_no_x(self):
        r1 = Rectangle(4, 2, y=5)
        self.assertEqual(r1.y, 5)

    def test_all_values_passes(self):
        r1 = Rectangle(4, 2, 2, 3, 7)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 7)

    def test_area(self):
        r1 = Rectangle(4, 2)
        r2 = Rectangle(3, 3, 2, 2, 5)
        self.assertEqual(r1.area(), 8)
        self.assertEqual(r2.area(), 9)

    def test_area_with_args(self):
        r1 = Rectangle(4, 3, 2, 3)
        with self.assertRaises(TypeError):
            r1.area('arg')

    def test_display(self):
        r1 = Rectangle(2, 2)
        r2 = Rectangle(4, 2, 0, 0, 5)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            expected = "##\n##\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), 6)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            expected = "####\n####\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), 10)

    def test_str(self):
        r1 = Rectangle(4, 2, 3, 3, 16)
        r2 = Rectangle(10, 4)
        r3 = Rectangle(6, 5, 7)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(r1)
            expected = f"[Rectangle] ({r1.id}) 3/3 - 4/2\n"
            self.assertEqual(mock_stdout.getvalue(), expected)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(r2)
            expected = f"[Rectangle] ({r2.id}) 0/0 - 10/4\n"
            self.assertEqual(mock_stdout.getvalue(), expected)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(r3)
            expected = f"[Rectangle] ({r3.id}) 7/0 - 6/5\n"
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_display1(self):
        r1 = Rectangle(2, 2, 2, 2)
        r2 = Rectangle(4, 2, 0, 3, 5)
        r3 = Rectangle(3, 3, 3)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            expected = "\n\n  ##\n  ##\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            expected = "\n\n\n####\n####\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r3.display()
            expected = "   ###\n   ###\n   ###\n"
            got = mock_stdout.getvalue()
            self.assertEqual(got, expected)
            self.assertEqual(len(got), len(expected))

    def test_update(self):
        r1 = Rectangle(4, 2, id=6)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 6)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        r1.update(3, 6)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 6)
        r1.update(7, 8, 9)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 9)
        r1.update(5, 4, 3, 2)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        r1.update(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_no_arg(self):
        r1 = Rectangle(4, 2, id=4)
        r1.update()
        self.assertEqual(r1.id, 4)
