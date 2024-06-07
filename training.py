import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Train.csv')

print(data)

data.head()

data.info()

data.isnull()

data.isnull().sum()

xpoints=data['BHK_NO.']
ypoints=data['TARGET(PRICE_IN_LACS)']

#plt.plot(xpoints,ypoints)
#plt.show()

#plt.scatter(xpoints,ypoints)
#plt.show()

#plt.hist(xpoints)
#plt.show()

#plt.fill_between(xpoints,ypoints)
#plt.show()

plt.bar(xpoints,ypoints)
plt.xlabel('BHK_NO.')
plt.ylabel('TARGET(PRICE_IN_LACS)')
plt.title('Bar Plot of BHK_NO. vs TARGET(PRICE_IN_LACS)')
plt.show()

#plt.barh(xpoints,ypoints)
#plt.show()

#plt.boxplot([xpoints,ypoints])
#plt.show()

#plt.hexbin(xpoints,ypoints,gridsize=18)
#plt.show()

#plt.pie(xpoints,ypoints)
#plt.show()
