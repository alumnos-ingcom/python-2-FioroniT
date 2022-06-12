################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import es_par

"""
Conjunto de tests para el ejercicio 1 del TP-python-2.
"""

def test_es_par_true():
    """
    Función que verifica si un número es par
    """
    numero = 10
    resultado = es_par(numero)
    assert isinstance(numero, int), "El valor de entrada debe ser un número entero mi rey"
    assert isinstance(resultado, bool), "El valor de salida debe ser un bool"
    assert resultado == True, "El valor de salida debe ser 'True' para el valor de entrada '10'"


def test_es_par_False():
    """
    Función que verifica si un número es par
    """
    numero = 11
    resultado = es_par(numero)
    assert isinstance(numero, int), "El valor de entrada debe ser un número entero mi rey"
    assert isinstance(resultado, bool), "El valor de salida debe ser un bool"
    assert resultado == False, "El valor de salida debe ser 'False' para el valor de entrada '11'"