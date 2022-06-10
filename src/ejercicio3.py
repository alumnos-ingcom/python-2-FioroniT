################
# Tomás  Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""
def super_puestos(lista_1, lista_2):
    i = 0
    superposicion = 0
    largo_lista_1 = len(lista_1)
    largo_lista_2 = len(lista_2)
    if largo_lista_1 < largo_lista_2:
        menor = largo_lista_1
    else:
        menor = largo_lista_2
    while i < menor:
        if lista_1[i] == lista_2[i]:
            superposicion += 1
            i += 1
        else:
            pass
    return superposicion
            


def principal():
    """
    Valor de entrada = list
    Valor de salida = int
    """
    lista_1 = input("Ingrese una lista: ")
    lista_2 = input("Ingrese otra lista: ")
    super_puestos(lista_1, lista_2)
    salida = super_puestos(lista_1, lista_2)
    print(salida)


if __name__ == "__main__":
    principal()


