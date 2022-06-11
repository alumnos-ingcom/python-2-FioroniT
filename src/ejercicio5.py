################
# Tomás  Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Implementar una función que determine si una cadena con corchetes está balanceada.
"""
def corchetes_balanceados(cadena):
    """
    Función donde se analiza repetidamente la cadena y se busca el balance de corchetes
    """
    balanceado = None
    i = 0
    corchete_abierto = "["
    corchete_cerrado = "]"
    posicion_corchete_abierto = cadena.find(corchete_abierto)
    posicion_corchete_cerrado = cadena.find(corchete_cerrado)
    lista_aux = list()
    contador_ca = 0
    contador_cc = 0
    j = posicion_corchete_abierto
    if posicion_corchete_abierto < posicion_corchete_cerrado:
        while i < len(cadena):
            if cadena[i] == corchete_abierto:
                contador_ca += 1
                i += 1
            else:
                i += 1
                continue
        while j < len(cadena):
            if cadena[j] == corchete_cerrado:
                contador_cc += 1
                j += 1
            else:
                j += 1
        if contador_ca == contador_cc:
            balanceado = True
        else:
            balanceado = False
    else:
        balanceado = False
    return balanceado


def principal():
    """
    Valor de entrada = str
    Valor de salida = bool
    """
    cadena = input("Introduzca una cadena a analizar: ")
    corchetes_balanceados(cadena)
    salida = corchetes_balanceados(cadena)
    print(salida)
if __name__ == "__main__":
    principal()

