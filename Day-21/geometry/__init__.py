# geometry/__init__.py

from .circle import area as circle_area, circumference
from .triangle import area as triangle_area, perimeter

__all__ = ["circle_area", "circumference", "triangle_area", "perimeter"]
