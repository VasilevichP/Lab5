import math
import random
import numpy as np


def form(x):
    y=((np.sin(np.pi/6-1))**2+(3+x**2)**(1./4)-(np.log10(x**3-1))**3)/(np.arcsin(x/2)-1.756E-2)
    return y

print(form(1.6453))

# --------------------------------------------------------------------

X=np.array([[1,random.randint(3,15),random.randint(60,82)] for i in range(12)])
print(X)
print("-------------------------------------------")
Y=np.array([[random.uniform(13.5,18.6)] for i in range(12)])
print(Y)
print("-------------------------------------------")
A=np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,Y))
print(A)
print("-------------------------------------------")
Y2=A[0]+A[1]*X[:,1]+A[2]*X[:,2]
print(Y2)