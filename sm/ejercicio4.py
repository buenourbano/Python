#ENUNCIADO
#Considere las listas "lst=['a',2,3,'xw','x',0,7,-1]" y "mst=['ab',4,2,'x',9,2,'x',0,7]". Haga una operación en la consola de Python que nos proporcione ordenados los índices de las entradas en la lista "lst" que aparecen como entradas en la lista "mst".

lst=['a',2,3,'xw','x',0,7,-1]
mst=['ab',4,2,'x',9,2,'x',0,7]

#Definimos una función que nos ordene los indices que almacenaremos

def OrdenarSinRepeticion(lista):
    listado=lista
    listado=list(set(listado))
    listado.sort()
    return(listado)

#Ahora definimos una función que nos haga el proceso deseado

def Indices(lista1,lista2):
    ListaDeIndices=[]
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            ListaDeIndices.append(i)
    if ListaDeIndices==[]:
        print('No hay ningún elemento de la primera lista que esté presente en la segunda.')
    else: 
        print(OrdenarSinRepeticion(ListaDeIndices))

#Aplicamos la función definida a nuestros ejemplos

Indices(lst,mst)