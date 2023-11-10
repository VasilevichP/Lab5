import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,5,6)
print(x)
y=x
z1=x**(1./4)+y**(1./4)
z2=x**2-y**2
z3=2*x+3*y
z4=x**2+y**2
z5=2+2*x+2*y-x**2-y**2

fig=plt.figure()
a1 = fig.add_subplot(2, 3, 1, projection='3d')
a1.plot(x,y,z1)
a2 = fig.add_subplot(2, 3, 2, projection='3d')
a2.plot(x,y,z2)
a3 = fig.add_subplot(2, 3, 3, projection='3d')
a3.plot(x,y,z3)
a4 = fig.add_subplot(2, 3, 4, projection='3d')
a4.plot(x,y,z4)
a5 = fig.add_subplot(2, 3, 5, projection='3d')
a5.plot(x,y,z5)

plt.show()