"""Module for Circle class."""

from math import pi

from src.shapes.base import Shape


class Circle(Shape):
    """Class for a circle shape."""

    def __init__(self, radius: float) -> None:
        """Initialize a circle object.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * self.radius**2

    def perimeter(self) -> float:
        """Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * pi * self.radius
