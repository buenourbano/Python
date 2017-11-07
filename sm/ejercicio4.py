#ENUNCIADO
#Diseñe un proceso que sea capaz de ordenar una lista eliminando las repeticiones.

def OrdenarSinRepeticion(lista):
    lst=lista
    lst=list(set(lst))
    lst.sort()
    return(lst)

#Veamos unos ejemplos

a=['a','b','d','d','c']
b=[1,2,2,2,2,2,1,1,1,1,3,4,9]
print(OrdenarSinRepeticion(a))
print(OrdenarSinRepeticion(b))