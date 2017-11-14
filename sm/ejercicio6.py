#ENUNCIADO
#Consiga conocer la letra del NIF correspondiente al DNI que es "42511275".

#Definimos la función

def LetraDNI(n):
    import string
    lst=list(string.ascii_uppercase) #Hacemos lista un string con todas las letras mayúsculas
    resto=n%23
    print("La letra del NIE {0} es {1}.".format(n,lst[resto]))

#Lo aplicamos al caso que se nos ha proporcionado

LetraDNI(42511275)
