################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import super_puestos

"""
Conjunto de tests para el ejercicio 3 del TP-python-2.
"""

def test_super_puestos():
    """
    Funcion de prueba de super_puestos()
    donde lista_1 es más larga que lista_2
    """
    lista_1 = "Hola Mundo"
    lista_2 = "Hola"
    resultado = super_puestos(lista_1, lista_2)
    assert isinstance (resultado, int), "El resultado debe ser un integer"
    assert resultado == 4, "El valor no es el esperado"

def test_super_puestos_al_reves():
    """
    Funcion de prueba de super_puestos()
    donde lista_2 es más larga que lista_1
    """
    lista_1 = "Hola"
    lista_2 = "Hola Mundo"
    resultado = super_puestos(lista_1, lista_2)
    assert isinstance (resultado, int), "El resultado debe ser un integer"
    assert resultado == 4, "El valor no es el esperado"

def test_super_puestos_incoincidentes():
    """
    Funcion de prueba de super_puestos()
    donde las listas son incoincidentes
    """
    lista_1 = "Hola Mundo"
    lista_2 = "PAN"
    resultado = super_puestos(lista_1, lista_2)
    assert isinstance (resultado, int), "El resultado debe ser un integer"
    assert resultado == 0, "El valor no es el esperado"

def test_super_puestos_coincidentes():
    """
    Funcion de prueba de super_puestos()
    donde las listas son coincidentes
    """
    lista_1 = "Hola Mundo"
    lista_2 = "Hola Mundo"
    resultado = super_puestos(lista_1, lista_2)
    assert isinstance (resultado, int), "El resultado debe ser un integer"
    assert resultado == 10, "El valor no es el esperado"