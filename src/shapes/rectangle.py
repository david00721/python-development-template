"""Module for Rectangle class."""

from src.shapes.base import Shape


class Rectangle(Shape):
    """Class for a rectangle shape."""

    def __init__(self, length: float, width: float) -> None:
        """Initialize a rectangle object.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)
