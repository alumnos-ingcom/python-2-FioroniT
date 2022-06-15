################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import encriptador, desencriptador
"""
Conjunto de tests para el ejercicio 6 del TP-python-2.
"""

def test_encriptador_mezcla():
    """
    Test de la función encriptadora utilizando mayúsculas, minúsculas y números
    """
    texto = "Tomy Fioroni 11"
    cantidad = 13
    resultado = encriptador(texto, cantidad)
    assert isinstance(resultado, list), "El valor de salida de esta función debe ser una lista"
    assert resultado == [71, 98, 122, 108, 32, 83, 118, 98, 101, 98, 97, 118, 32, 52, 52], "La salida no es la esperada"

def test_encriptador_caracter_invalido():
    """
    Test de la función encriptadora utilizando un caracter no válido
    """
    texto = []
    cantidad = 13
    resultado = encriptador(texto, cantidad)
    assert isinstance(resultado, list), "El valor de salida de esta función debe ser una lista"
    assert resultado == [], "La salida no es la esperada"

def test_desencriptador():
    """
    Test de la función desencriptadora
    """
    texto = "Tomy Fioroni 11"
    cantidad = 13
    unicode = [71, 98, 122, 108, 32, 83, 118, 98, 101, 98, 97, 118, 32, 52, 52]
    resultado = desencriptador(texto, unicode)
    assert isinstance(resultado, str), "El valor de salida de esta función debe ser una lista"
    assert resultado == '', "La salida no es la esperada"