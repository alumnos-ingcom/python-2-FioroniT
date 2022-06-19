################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import fibonacci

"""
Conjunto de tests para el ejercicio 4 del TP-python-2.
"""
def test_fibonacci_valido():
    """
    Test para la función en caso de que el valor de entrada sea válido
    """
    n = 5
    resultado = fibonacci(n)
    assert isinstance (resultado, int), "El valor de salida debe ser un integer"
    assert resultado == 13, "La salida no es la esperada"

def test_fibonacci_no_valido():
    """
    Test para la función en caso de que el valor de entrada sea inválido
    """
    n = 0
    resultado = fibonacci(n)
    assert isinstance (resultado, int), "El valor de salida debe ser un integer"
    assert resultado == 0, "La salida no es la esperada"
    