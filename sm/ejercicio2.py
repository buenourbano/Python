#ENUNCIADO
#Rediseñe la anterior función para que proporcione un generador, caso de no incluir ya esa funcionalidad.

def floatingrange2(comienzo,final,paso=0.1):
    elemento = comienzo
    if paso==0:
        paso=0.1
    else:
        while elemento < final:
            yield elemento
            elemento += paso
