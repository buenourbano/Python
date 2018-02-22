# -*- coding: utf-8 -*-

"""
Software en Matemáticas
Jesús Bueno Urbano - 20078941X
"""

"""
Ejemplos de uso:

python3 ex4.py 07/02/2018

python3 ex4.py [07/02/2018,18/02/2018] 'Granada'

"""


import re
import sys
from urllib.request import urlretrieve
from os import popen
import PyPDF2
import os

def zellerGregorian(d,m,a):
    if m in [1,2]:
        m += 12
        a -= 1
    q, m, a = d,m,a
    J, K = divmod(a,100)
    c1,r1 = divmod((m+1)*26,10)
    c2,r2 = divmod(K,4)
    c3,r3 = divmod(J,4)
    r = (q+c1+K+c2+c3-2*J) % 7
    return ['sat','sun','mon','tue','wed','thu','fri'][r]

def weekDay(s):
        dict = {'sat':False,'sun':False,'mon':True,'tue':True,'wed':True,'thu':True,'fri':True}
        return dict[s]

def holyday(s):
        holydaysNat = ['1/1','6/1','1/5','15/8','12/10','1/11','6/12','8/12','25/12']
        holydaysReg = ['28/2']
        holydaysLoc = ['2/1','28/2','15/9']
        t = '/'.join(s.split('/')[:-1])
        return not (t in holydaysNat or t in holydaysReg or t in holydaysLoc)

def yearHolyday2018(s):
        yearHolyday=['29/3/2018','30/3/2018','31/5/2018']
        return not (s in yearHolyday)

def warning(date):
        d,m,a = date.split('/')
        d,m,a = int(d), int(m), int(a)
        return weekDay(zellerGregorian(d,m,a)) and holyday(date) and yearHolyday2018(date)
    
"""    
AQUÍ COMIENZA EL SCRIPT PROPIAMENTE DICHO 
"""

if __name__ == "__main__":
    date = sys.argv[1]
    #Como en un script se reconoce cada elemento como un string, hacemos una lista de fechas
    date2 = list(map(str, date.strip('[]').split(',')))
    
    #Hacemos un try por si el usuario no introduce ninguna palabra o listas de palabras
    try:
        words = sys.argv[2]
        #Como en un script se reconoce cada elemento como un string, hacemos una lista de palabras
        words2 = list(map(str, words.strip("['']").split("','")))
        
        for i in range(len(date2)):
            #Recorremos la lista de fechas
        
            boplink = 'http://bop2.dipgra.es:8880/opencms/opencms/portal/DescargaPDFBoletin?fecha='
            currentdate = date2[i]
            boplink = ''.join([boplink,currentdate])
            dateg = '-'.join(currentdate.split('/'))
            nameFile = '_'.join(['bop',dateg])
            nameFile = '.'.join([nameFile,'pdf'])
        
            if warning(currentdate):
                urlretrieve (boplink, nameFile)
                #Descargamos el archivo si ese día se ha publicado
                
                currentPDF = open(nameFile, 'rb')
                PDFreader = PyPDF2.PdfFileReader(currentPDF)
                textototal = []
                estado = []
            
                for i in range(PDFreader.numPages):
                    texto = PDFreader.getPage(i).extractText()
                    texto = texto.split(' ')
                    textototal = textototal + texto
                    #Creamos una lista con todas las palabras del PDF
                
                for elemento in words2:
                    if elemento in textototal:
                        estado = estado + [1]
                    else:
                        estado = estado + [0]
                    #Buscamos las palabras en el texto
                    
                if min(estado)==0:
                    os.remove(nameFile)
            else:
                print('Advertencia: El día {0} no se editó el BOP.'.format(currentdate))
                #Mensaje que mopstramos en caso de que ese día no se haya publicado
            
    except:
        for i in range(len(date2)):
        
            boplink = 'http://bop2.dipgra.es:8880/opencms/opencms/portal/DescargaPDFBoletin?fecha='
            currentdate = date2[i]
            boplink = ''.join([boplink,currentdate])
            dateg = '-'.join(currentdate.split('/'))
            nameFile = '_'.join(['bop',dateg])
            nameFile = '.'.join([nameFile,'pdf'])

            if warning(currentdate):
                urlretrieve (boplink, nameFile)
            else:
                print('Advertencia: El día {0} no se editó el BOP.'.format(currentdate))