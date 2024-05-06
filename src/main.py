"""Main module to run the program."""

from src.shapes.circle import Circle
from src.shapes.rectangle import Rectangle


def main() -> None:
    """Main function to run the program."""
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    circle_perimeter = circle.perimeter()
    circle_area = circle.area()

    rectangle_perimeter = rectangle.perimeter()
    rectangle_area = rectangle.area()

    print(f"Circle Perimeter: {round(circle_perimeter, 2)}m")
    print(f"Circle Area: {round(circle_area, 2)}m2")
    print(f"Rectangle Perimeter: {rectangle_perimeter}m")
    print(f"Rectangle Area: {rectangle_area}m2")


if __name__ == "__main__":
    main()
