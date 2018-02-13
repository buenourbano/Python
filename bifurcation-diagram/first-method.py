from numpy import *
from pylab import *

def bifurcacion(b,n):
    
    X, Y = [], []
    A = linspace(2.5,4,10000)
    
    for a in A:
        x = random()
        for j in range(n):
            x = x * (a - b*x)
        X.append(a)
        Y.append(x)
    plot(X,Y,ls='', marker='*',color = 'g',markersize = 0.5)
    show()