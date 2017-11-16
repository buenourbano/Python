#ENUNCIADO
#Consiga conocer la letra del NIF correspondiente al DNI que es "42511275".

#Definimos la función

def LetraDNI(n):
    lst=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    resto=n%23
    print("La letra del NIE {0} es {1}.".format(n,lst[resto]))

#Lo aplicamos al caso que se nos ha proporcionado

LetraDNI(42511275)
