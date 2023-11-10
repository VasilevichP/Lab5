import random

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
pnd.options.display.max_rows=1000
pnd.options.display.max_columns=20
ds=pnd.read_csv("test.csv",sep=",")
ds=ds.head(1000)
ds=ds.fillna(0)

ds.info()

# ds.Id.plot.box(return_type='both')
for i in range(19):
    plt.subplot(4,5,i+1)
    plt.hist(ds.iloc[:,i],bins=100)
plt.show()

ds=ds[ds["Rooms"]>0]
ds["Square"][(ds["Square"]>200)|(ds["Square"]<30)]=random.randint(30,200)
ds["KitchenSquare"][(ds["KitchenSquare"]>30)|(ds["KitchenSquare"]<5)]=random.randint(5,30)
ds["LifeSquare"][(ds["LifeSquare"]>30)|(ds["LifeSquare"]<8)]=random.randint(8,30)
ds["HouseFloor"][(ds["HouseFloor"]>100)|(ds["HouseFloor"]<1)]=random.randint(1,100)
ds["HouseYear"][(ds["HouseYear"]>2023)|(ds["HouseYear"]<1800)]=random.randint(1800,2023)
ds.info()
print(ds)
print("--------------------------------------------")
print(ds["Rooms"].value_counts())

print("--------------------------------------------")

pt=ds.pivot_table(index=["DistrictId"],columns=["Rooms"],aggfunc={"Rooms":len},fill_value=0)
print(pt)
ds.to_csv("vasilevich.csv")