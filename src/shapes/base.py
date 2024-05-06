"""Module for the Shape class."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract baseclass for shapes.

    Attributes:
        None

    Methods:
        area: Abstract method to calculate the area of a shape.
        perimeter: Abstract method to calculate the perimeter of a shape.
    """

    @abstractmethod
    def area(self) -> float:
        """Abstract method to calculate the area of a shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to calculate the perimeter of a shape."""
