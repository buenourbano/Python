#ENUNCIADO
#Diseñe un proceso que simule el funcionamiento de "range" y que permita el uso de parámetro de tipo float.

def fgrange(comienzo,final,paso=0.1):
    elemento = comienzo
    resultado = []
    if paso==0:
        paso=0.1
    else:
        while elemento < final:
            resultado.append(elemento)
            elemento += paso
    return resultado
