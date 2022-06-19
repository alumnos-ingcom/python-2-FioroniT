################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import encriptador, desencriptador, traductor
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
    cantidad = 13
    encriptado = "Gbzl Svbebav 44"
    resultado = desencriptador(encriptado, cantidad)
    assert isinstance(resultado, list), "El valor de salida de esta función debe ser una lista"
    assert resultado == [84, 111, 109, 121, 32, 70, 105, 111, 114, 111, 110, 105, 32, 49, 49], "La salida no es la esperada"

def test_traductor_encriptado():
    """
    Test de la funcion de traductor cuando se le da un texto encriptado
    """
    texto = "Tomy Fioroni 11"
    unicode = [71, 98, 122, 108, 32, 83, 118, 98, 101, 98, 97, 118, 32, 52, 52]
    resultado = traductor(texto, unicode)
    assert isinstance(resultado, str), "El valor de salida de esta función debe ser una cadena"
    assert resultado == "Gbzl Svbebav 44", "La salida no es la esperada"

def test_traductor_desencriptado():
    """
    Test de la funcion de traductor cuando se le da un texto encriptado
    """
    texto = "Tomy Fioroni 11"
    unicode = [84, 111, 109, 121, 32, 70, 105, 111, 114, 111, 110, 105, 32, 49, 49]
    resultado = traductor(texto, unicode)
    assert isinstance(resultado, str), "El valor de salida de esta función debe ser una cadena"
    assert resultado == "Tomy Fioroni 11", "La salida no es la esperada"