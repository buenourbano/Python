#ENUNCIADO
#Diseñe un proceso que simule el funcionamiento de "range" y que permita el uso de parámetro de tipo float.

def floatingrange(comienzo,final,paso):
    elemento = float(comienzo)
    parada = float(final)
    pasolocal = float(paso)
    resultado = []
    while elemento < parada:
        resultado.append(elemento)
        elemento += pasolocal
    return resultado
