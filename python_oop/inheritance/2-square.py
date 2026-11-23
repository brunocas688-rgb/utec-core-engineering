#!/usr/bin/env python3
"""Módulo que define Square con representación en cadena."""

try:
    from square import Square as _BaseSquare
except ImportError:
    try:
        mod = __import__(
            "1-square",
            fromlist=["Square"],
        )
        _BaseSquare = mod.Square
    except ImportError:
        mod = __import__(
            "python_oop.inheritance.1-square",
            fromlist=["Square"],
        )
        _BaseSquare = mod.Square


class Square(_BaseSquare):
    """Representa un cuadrado con formato [Square] <width>/<height>."""

    def __init__(self, size):
        """Inicializa el cuadrado con size validado."""
        super().__init__(size)
        self.__size = size

    def __str__(self):
        """Devuelve la descripción [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"
