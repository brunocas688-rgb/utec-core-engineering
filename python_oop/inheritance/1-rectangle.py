#!/usr/bin/env python3
"""Módulo que define la clase Rectangle heredada de BaseGeometry."""

try:
    from base_geometry import BaseGeometry
except ImportError:
    BaseGeometry = __import__(
        "python_oop.inheritance.base_geometry", fromlist=["BaseGeometry"]
    ).BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo validado con BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa width y height privados tras validarlos."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
