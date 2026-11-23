#!/usr/bin/env python3
"""Módulo base para clases de figuras geométricas."""


class BaseGeometry:
    """Clase base para figuras geométricas."""

    def area(self):
        """Indica que el cálculo del área no está implementado en la clase base."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero estrictamente mayor que 0."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
