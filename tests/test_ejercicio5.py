################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import corchetes_balanceados
"""
Conjunto de tests para el ejercicio 5 del TP-python-2.
"""
def test_corchetes_balanceados_true():
    """
    Test de la función de corchetes balanceados con resultado verdadero
    """
    cadena = "Hola [Mundo]"
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == True, "El valor debe ser Verdadero"

def test_corchetes_balanceados_false():
    """
    Test de la función de corchetes balanceados con resultado falso
    """
    cadena = "Hola ]Mundo["
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == False, "El valor debe ser Falso"

def test_corchetes_balanceados_vacio():
    """
    Test de la función de corchetes balanceados sin corchetes
    """
    cadena = "Hola Mundo"
    resultado = corchetes_balanceados(cadena)
    assert isinstance (resultado, bool), "El Valor de salida debe ser un bool"
    assert resultado == True, "El valor debe ser Verdadero"