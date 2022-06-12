#data science zscore

data = {'X1': [155,15,13,11,12,11,15,156,13,10,12],

       'X2': [149,169,172,148,156,162,189,555,147,150,153]}
datas = [data["X1"],data["X2"]]
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(data)

from scipy import stats
d = []
results = []
z = np.abs(stats.zscore(dataframe))
threshold = 2
check = np.where(z > threshold)
for i in range (0,len(check)):
    d.append(check[i])

for j in range(0,(len(d[0]))):
    results.append((d[0][j],d[1][j]))
print(results)
