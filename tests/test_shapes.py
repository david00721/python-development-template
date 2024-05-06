import unittest

from src.shapes.circle import Circle
from src.shapes.rectangle import Rectangle


class CircleTests(unittest.TestCase):
    def test_area(self) -> None:
        circle = Circle(5.0)
        self.assertAlmostEqual(circle.area(), 78.54, places=2)

    def test_perimeter(self) -> None:
        circle = Circle(5.0)
        self.assertAlmostEqual(circle.perimeter(), 31.42, places=2)


class RectangleTests(unittest.TestCase):
    def test_area(self) -> None:
        rectangle = Rectangle(4.0, 6.0)
        self.assertEqual(rectangle.area(), 24)

    def test_perimeter(self) -> None:
        rectangle = Rectangle(4.0, 6.0)
        self.assertEqual(rectangle.perimeter(), 20)


if __name__ == "__main__":
    unittest.main()
