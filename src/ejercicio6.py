################
# Tomás  Fioroni - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
"""
def encriptador(texto, cantidad):
    """
    Función que encripta caracteres entre 'AZaz09'
    Con la rotación deseada por el usuario
    """
    cantidad_original = cantidad
    limite = len(texto)
    i = 0
    unicode = []
    while limite > 0:
        caracter = ord(texto[i])
        if texto[i].isupper():
            minimo = 65
            while caracter <= 90 and cantidad > 0:
                caracter += 1
                cantidad -= 1
                if caracter > 90:
                    caracter = minimo
                else:
                    continue
        elif texto[i].islower():
            minimo = 97
            while caracter <= 122 and cantidad > 0:
                caracter += 1
                cantidad -= 1
                if caracter > 122:
                    caracter = minimo
                else:
                    continue
        elif texto[i].isdigit():
            minimo = 48
            while caracter <= 57 and cantidad > 0:
                caracter += 1
                cantidad -= 1
                if caracter > 57:
                    caracter = minimo
                else:
                    continue
        else:
            pass
        limite -= 1
        i += 1
        cantidad = cantidad_original
        unicode.append(caracter)
    return unicode


def desencriptador(encriptado, cantidad):
    """
    Función que desencripta el mensaje en una cadena
    """
    cantidad_original = cantidad
    limite = len(encriptado)
    i = 0
    desencriptado = []
    while limite > 0:
        caracter = ord(encriptado[i])
        if encriptado[i].isupper():
            maximo = 90
            while caracter >= 65 and cantidad > 0:
                caracter -= 1
                cantidad -= 1
                if caracter < 65:
                    caracter = maximo
                else:
                    continue
        elif encriptado[i].islower():
            maximo = 122
            while caracter >= 97 and cantidad > 0:
                caracter -= 1
                cantidad -= 1
                if caracter < 97:
                    caracter = maximo
                else:
                    continue
        elif encriptado[i].isdigit():
            maximo = 57
            while caracter >= 48 and cantidad > 0:
                caracter -= 1
                cantidad -= 1
                if caracter < 48:
                    caracter = maximo
                else:
                    continue
        else:
            pass
        limite -= 1
        i += 1
        cantidad = cantidad_original
        desencriptado.append(caracter)
    return desencriptado




def traductor(texto, unicode):
    """
    Función que desencripta el texto encriptado por el usuario
    """
    limite = len(texto)
    i = 0
    encriptado = []
    salida = ""
    while limite > 0:
        caracter = chr(unicode[i])
        encriptado.append(caracter)
        limite -= 1
        i += 1
    salida = salida.join(encriptado)
    return salida


def principal():
    """
    Valor de entrada = str
    Valor de salida = list, str
    """
    texto = input("Introduzca un texto a cifrar: ")
    cantidad = int(input("Introduzca una cantidad de carácteres para cifrar: "))
    unicode = encriptador(texto, cantidad)
    print(unicode)
    encriptado = traductor(texto, unicode)
    print(encriptado)
    unicode_desencriptado = desencriptador(encriptado, cantidad)
    print(unicode_desencriptado)
    final = traductor(texto, unicode_desencriptado)
    print(final)
if __name__ == "__main__":
    principal()

