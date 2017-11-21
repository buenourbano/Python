def ordenarsinrepetir(lista):
    lista=list(set(lista))
    lista.sort()
    return lista

#Hacemos un ejemplo

r=[64,9,93,8,8,64,1]
print('Lista sin ordenar: ',r)
ordenarsinrepetir(r)
print('Lista ordenada: ',ordenarsinrepetir(r))