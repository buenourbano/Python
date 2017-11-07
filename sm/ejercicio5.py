#ENUNCIADO
#Considere las listas "lst=['a',2,3,'xw','x',0,7,-1]" y "mst=['ab',4,2,'x',9,2,'x',0,7]". Haga una operación en la consola de Python que nos proporcione ordenados los índices de las entradas en la lista "lst" que aparecen como entradas en la lista "mst".

lst=['a',2,3,'xw','x',0,7,-1]
mst=['ab',4,2,'x',9,2,'x',0,7]

ListaDeIndices=[]

for i in range(len(lst)):
    if lst[i] in mst:
        ListaDeIndices.append(i)

#Hacemos uso de la función definida en el ejercicio 4

def OrdenarSinRepeticion(lista):
    lst=lista
    lst=list(set(lst))
    lst.sort()
    return(lst)

if ListaDeIndices==[]:
    print('No hay ningún elemento de la lista lst que esté presente en la lista mst.')
else: 
    print(OrdenarSinRepeticion(ListaDeIndices))
        
