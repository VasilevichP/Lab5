import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd

def fun(x,a):
    return round(np.exp(a*x)-3.45*a,1)

li=[]
a=0

while (a<=2):
    li.append([a,fun(3.67,a)])
    a=a+0.2
arr=np.array(li)

print(arr)
print("----------------------------------")
print("Max: ",arr[:,1].max())
print("Min: ",arr[:,1].min())
print("Average: ",arr[:,1].mean())
print("Num of elements:", arr.shape[0])
print("----------------------------------\nSorted")
arr=arr[arr[:,1].argsort(),:]
print(arr)

x=arr[:,0]
y=arr[:,1]
y2=[arr[:,1].mean() for i in range(11)]

plt.subplot(1,2,1)
plt.plot(x,y,marker='o',color="#ee1e2e",label="Значения f(x,а)")
plt.axis([0,2,1,1539])
plt.title("Значения f(x,а)")
plt.xlabel("a")
plt.ylabel("f(x,a)")

plt.subplot(1,2,2)
plt.plot(x,y2,marker='1',color="#ee1e2e",label="Среднее значение f(x,а)")
plt.axis([0,2,200,300])
plt.title("Среднее значение f(x,а)")
plt.xlabel("a")
plt.ylabel("avg(f)")

plt.show()