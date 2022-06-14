################
# Tomás Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.
"""
def cargador():
    """
    Función que crea la secuencia a trabajar
    """
    print("""Ingrese '0' para cortar la secuencia""")
    secuencia = list()
    numero = None
    while numero != 0:
            numero = int(input("Ingrese un número de la secuencia: "))
            secuencia.append(numero)
    secuencia.remove(0)
    return secuencia


def minimo(secuencia):
    """
    Función que busca el minimo de la secuencia
    """
    j = 1
    menor = secuencia[0]
    fin = len(secuencia)
    while j < fin:
        if menor > secuencia[j]:
            menor = secuencia[j]
        else:
            j += 1
    return menor
        

def maximo(secuencia):
    """
    Función que busca el máximo de la secuencia
    """
    j = 1
    mayor = secuencia[0]
    fin = len(secuencia)
    while j < fin:
        if mayor < secuencia[j]:
            mayor = secuencia[j]
        else:
            j += 1
    return mayor


def promedio(secuencia):
    """
    Función que calcula el promedio de la secuencia
    """
    i = 0
    suma = int()
    while i < len(secuencia):
        suma += (secuencia[i])
        i += 1
    promedio = suma // len(secuencia)
    return promedio   


def tuplador(minimo_secuencia, maximo_secuencia, promedio_secuencia):
    tupla = [minimo_secuencia, maximo_secuencia, promedio_secuencia]
    resultado = tuple(tupla)
    return resultado


def principal():
    """
    Valor de entrada: int
    Valor de salida: tuple
    """
    secuencia = cargador()
    minimo_secuencia = minimo(secuencia)
    maximo_secuencia = maximo(secuencia)
    promedio_secuencia = promedio(secuencia)
    resultado = tuplador(minimo_secuencia, maximo_secuencia, promedio_secuencia)
    print(resultado)


if __name__ == "__main__":
    principal()

