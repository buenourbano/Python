#ENUNCIADO
#Diseñe un proceso que simule el funcionamiento del método "count()".

def contador(lista,elemento):
    lst=lista
    unidad=elemento
    resultado=0
    for i in range(len(lst)):
        if lst[i]==unidad:
            resultado += 1
    print("El elemento {0} aparece {1} veces.".format(unidad,resultado))


#veamos un ejemplo

lst=['a','a',2,3,'xw','x',0,7,-1]
contador(lst,'a')