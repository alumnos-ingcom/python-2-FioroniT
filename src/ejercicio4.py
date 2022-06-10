################
# Tomás  Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores.
En la misma, los dos primeros términos son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""

def fibonacci(n):
    """
    Esta función va a conseguir la n-ésima sucesión de Fibonacci, indicada por el usuario
    """
    i = 0
    contador = 0
    numero_1 = 0
    numero_2 = 1
    assert n >= 1, "Este número no es un entero positivo mayor a 2."
    while i <= n:
        contador = numero_1 + numero_2
        numero_1 = numero_2
        numero_2 = contador
        i += 1
    assert contador >= 2, "Este número no es un entero positivo mayor a 2."
    return contador
        

def principal():
    """
    Valor de entrada = int
    Valor de salida = int
    """
    n = int(input("Indique que término de la sucesion quiere: "))
    fibonacci(n)
    salida = fibonacci(n)
    print(salida)


if __name__ == "__main__":
    principal()

