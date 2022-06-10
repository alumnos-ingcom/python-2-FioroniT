################
# Tomás  Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Definir si el numero es par o impar sin usar '%' retornando un booleano
"""
def es_par(numero):
    """
    Funcion que va a determinar si el  número ingresado es par o no
    """
    cociente = numero / 2
    decimal = abs(cociente) - abs(int(cociente))
    if decimal == 0:
        return True
    else:
        return False
def principal():
    """
    En esta función define el número (int)
    que va a ser procesado y devuelve un bool
    """
    numero = int(input("Ingrese un número: "))
    es_par(numero)
if __name__ == "__main__":
    principal()

