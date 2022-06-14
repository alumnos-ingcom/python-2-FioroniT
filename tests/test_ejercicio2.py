################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import minimo, maximo, promedio, tuplador

"""
Conjunto de tests para el ejercicio 2 del TP-python-2.
"""
def test_minimo():
    secuencia = [10, 11, 9]
    resultado = minimo(secuencia)
    assert isinstance(resultado, int), "El valor de salida debe ser un integer"
    assert resultado == 9, "El valor no es el esperado"

def test_maximo():
    secuencia = [10, 11, 9]
    resultado = maximo(secuencia)
    assert isinstance(resultado, int), "El valor de salida debe ser un integer"
    assert resultado == 11, "El valor no es el esperado"

def test_promedio():
    secuencia = [10, 11, 9]
    resultado = promedio(secuencia)
    assert isinstance (resultado, int), "El valor de salida debe ser un integer"
    assert resultado == 10, "El valor no es el esperado"

def test_tuplador():
    minimo = 9
    maximo = 11
    promedio = 10
    resultado = tuplador(minimo, maximo, promedio)
    assert isinstance (resultado, tuple), "El valor de salida debe ser una tupla"
    assert resultado == (9, 11, 10), "El valor no es el esperado"
    