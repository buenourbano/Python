#ENUNCIADO
#Rediseñe la anterior función para que proporcione un generador, caso de no incluir ya esa funcionalidad.

def floatingrange2(comienzo,final,paso):
    elemento = float(comienzo)
    parada = float(final)
    pasolocal = float(paso)
    while elemento < parada:
        yield elemento
        elemento += pasolocal