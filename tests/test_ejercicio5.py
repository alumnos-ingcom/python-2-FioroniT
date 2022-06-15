################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import corchetes_balanceados
"""
Conjunto de tests para el ejercicio 4 del TP-python-2.
"""
def test_corchetes_balanceados_true():
    cadena = "Hola [Mundo]"
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == True, "El valor debe ser Verdadero"

def test_corchetes_balanceados_false():
    cadena = "Hola ]Mundo["
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == False, "El valor debe ser Falso"

def test_corchetes_balanceados_vacio():
    cadena = "Hola Mundo"
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == True, "El valor debe ser Verdadero"