#!/usr/bin/env python3
"""Módulo que define la clase completa Rectangle."""

try:
    from base_geometry import BaseGeometry
except ImportError:
    mod = __import__(
        "python_oop.inheritance.base_geometry",
        fromlist=["BaseGeometry"],
    )
    BaseGeometry = mod.BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con área y representación en cadena."""

    def __init__(self, width, height):
        """Inicializa width y height privados tras validarlos."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripción [Rectangle] <width>/<height>."""
        return f"[Rectangle] {self.__width}/{self.__height}"
