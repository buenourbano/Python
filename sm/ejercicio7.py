#ENUNCIADO
#Consiga conocer la letra del NIF correspondiente al DNI que es "42511275".
import string

lst=list(string.ascii_uppercase)

def LetraDNI(n):
    resto=n%23
    return(lst[resto])

#Lo aplicamos al caso que se nos ha proporcionado

print("La letra del NIE {0} es {1}.".format(42511275,LetraDNI(42511275))) 
