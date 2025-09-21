from __future__ import annotations
import math
from functools import total_ordering


@total_ordering
class Circle:
    """
    A simple circle defined by its radius.

    Features:
    - radius (stored)
    - diameter (property get/set)
    - area (read-only property)
    - classmethod from_diameter
    - pretty __str__ / __repr__
    - + add two circles (sum of radii) -> same type as left operand
    - * scale by number (both sides supported)
    - comparisons by radius (sortable)
    """

    def __init__(self, radius: float):
        if radius is None:
            raise TypeError("radius is required")
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self._radius = float(radius)

    # radius (stored) — expose via property to keep symmetry with diameter
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("radius must be non-negative")
        self._radius = float(value)

    # diameter computed from radius; setting diameter adjusts radius
    @property
    def diameter(self) -> float:
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value: float) -> None:
        if value < 0:
            raise ValueError("diameter must be non-negative")
        self._radius = float(value) / 2.0

    # read-only area
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @classmethod
    def from_diameter(cls, d: float) -> "Circle":
        if d < 0:
            raise ValueError("diameter must be non-negative")
        return cls(d / 2.0)

    # pretty printing
    def __str__(self) -> str:
        # match expected output exactly:
        # "circle.Circle with radius: 5"
        return f"{self.__module__}.{self.__class__.__name__} with radius: {int(self.radius) if self.radius.is_integer() else self.radius}"

    def __repr__(self) -> str:
        # match expected output exactly:
        # "circle.Circle(5)"
        r = int(self.radius) if self.radius.is_integer() else self.radius
        return f"{self.__module__}.{self.__class__.__name__}({r})"

    # numeric protocol
    def __add__(self, other: "Circle") -> "Circle":
        if not isinstance(other, Circle):
            return NotImplemented
        # preserve the class of the left operand (Circle or Sphere)
        return self.__class__(self.radius + other.radius)

    def __mul__(self, factor: float) -> "Circle":
        if not isinstance(factor, (int, float)):
            return NotImplemented
        if factor < 0:
            raise ValueError("scale factor must be non-negative")
        return self.__class__(self.radius * factor)

    def __rmul__(self, factor: float) -> "Circle":
        return self.__mul__(factor)

    # comparisons (by radius)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def __lt__(self, other: "Circle") -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


class Sphere(Circle):
    """
    A sphere — inherits Circle’s radius/diameter behavior.

    Adds:
    - surface area (overrides area property): 4πr²
    - volume property: (4/3)πr³
    - Sphere-specific __str__/__repr__
    """

    @property
    def area(self) -> float:
        # surface area of a sphere:
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self) -> float:
        return (4.0 / 3.0) * math.pi * (self.radius ** 3)

    def __str__(self) -> str:
        # expected: "Sphere with radius: 5" when printed in test messages
        # (tests print f"{s1}" inside text that doesn’t need module prefix)
        return f"Sphere with radius: {int(self.radius) if self.radius.is_integer() else self.radius}"

    def __repr__(self) -> str:
        r = int(self.radius) if self.radius.is_integer() else self.radius
        return f"Sphere({r})"
