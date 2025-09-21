from __future__ import annotations
import math
from functools import total_ordering

def _repr_radius_as_int_if_whole(r: float) -> str:
    return str(int(r)) if float(r).is_integer() else str(r)

@total_ordering
class Circle:
    def __init__(self, radius: float = None, diameter: float = None):
        if radius is not None:
            self._radius = float(radius)
        elif diameter is not None:
            self._radius = float(diameter) / 2.0
        else:
            raise ValueError("Provide radius or diameter")

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        return self._radius * 2.0

    @diameter.setter
    def diameter(self, value: float) -> None:
        self._radius = float(value) / 2.0

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @classmethod
    def from_diameter(cls, d: float) -> "Circle":
        return cls(diameter=d)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with radius: {self.radius:.6f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({_repr_radius_as_int_if_whole(self.radius)})"

    def __add__(self, other: "Circle") -> "Circle":
        if isinstance(other, self.__class__):
            return self.__class__(self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle (or same subclass).")

    def __mul__(self, scalar: float) -> "Circle":
        if isinstance(scalar, (int, float)):
            return self.__class__(self.radius * float(scalar))
        raise TypeError("Can only multiply by a number.")

    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other: "Circle") -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

@total_ordering
class Sphere(Circle):
    @property
    def area(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self) -> float:
        return (4.0 / 3.0) * math.pi * (self.radius ** 3)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with radius: {self.radius:.6f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({_repr_radius_as_int_if_whole(self.radius)})"

    @classmethod
    def from_diameter(cls, d: float) -> "Sphere":
        return cls(diameter=d)

    def __add__(self, other: "Sphere") -> "Sphere":
        if isinstance(other, Sphere):
            return self.__class__(self.radius + other.radius)
        raise TypeError("Can only add Sphere to Sphere.")
