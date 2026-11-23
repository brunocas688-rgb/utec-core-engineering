#!/usr/bin/env python3
"""Módulo que define la clase Square heredada de Rectangle."""

try:
    from rectangle import Rectangle
except ImportError:
    try:
        mod = __import__(
            "2-rectangle",
            fromlist=["Rectangle"],
        )
        Rectangle = mod.Rectangle
    except ImportError:
        mod = __import__(
            "python_oop.inheritance.2-rectangle",
            fromlist=["Rectangle"],
        )
        Rectangle = mod.Rectangle


class Square(Rectangle):
    """Representa un cuadrado basado en Rectangle."""

    def __init__(self, size):
        """Inicializa size privado validado con integer_validator."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
