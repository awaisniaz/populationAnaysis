import pandas as pd
import numpy as np
data = pd.read_csv('california_cities.csv',index_col='Unnamed: 0')
print(data.head())
print(data.info())
print(data.describe())

latitude,longitude = data['latd'],data['longd']
popultion,area = data['population_total'],data['area_total_km2']

# TO Scatter the points,using size and colour but without label
import seaborn
import matplotlib.pyplot as plt
seaborn.set()

plt.scatter(longitude,latitude,label=None,c = np.log10(popultion),cmap='viridis',s=area,linewidths=0,alpha=0.5)
plt.xlabel('Logitude')
plt.ylabel('latitide')
plt.colorbar(label='Population')
plt.clim(3,7)

for area in [100,200,300]:
    plt.scatter([],[],c='red',alpha=0.3,s=area,label=str(area)+'kms')
plt.legend(scatterpoints =1,frameon = False,labelspacing=1,title ="City Area")
plt.title('Area and Population of California Cities')
plt.show()
