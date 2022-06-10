################
# Tomás Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Enunciado del ejercicio
"""
def cargador():
    print("""Ingrese '0' para cortar la secuencia""")
    secuencia = list()
    numero = None
    while numero != 0:
            numero = int(input("Ingrese un número de la secuencia: "))
            secuencia.append(numero)
    secuencia.remove(0)
    return secuencia


def minimo(secuencia):
    i = 0
    i2 = 1
    minimo = secuencia[1]
    while i2 < len(secuencia):
        if secuencia[i] < secuencia[i2]:
            i2 += 1
            minimo = secuencia[i]
        else:
            i = i2
            i2 += 1
    return minimo


def maximo(secuencia):
    i = 0
    i2 = 1
    maximo = secuencia[1]
    while i2 < len(secuencia):
        if secuencia[i] > secuencia[i2]:
            i2 += 1
            maximo = secuencia[i]
        else:
            i = i2
            i2 += 1
    return maximo


def promedio(secuencia):
    i = 0
    suma = int()
    while i < len(secuencia):
        suma += (secuencia[i])
        i += 1
    promedio = suma // len(secuencia)
    return promedio   



def principal():
    """
    Docstring
    """
    secuencia = cargador()
    print(secuencia)
    minimo_secuencia = minimo(secuencia)
    print(f"El minimo es {minimo_secuencia}")
    maximo_secuencia = maximo(secuencia)
    print(f"El máximo es {maximo_secuencia}")
    promedio_secuencia = promedio(secuencia)
    print(f"El promedio es {promedio_secuencia}")


if __name__ == "__main__":
    principal()