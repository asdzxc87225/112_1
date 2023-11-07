import pyexcel
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_excel("縣市人口性比例及人口密度-112年9月.ods", engine="odf")
column_names = data.columns

# 打印列名
print(column_names)
a=list(data['    戶數、人口數、性別比例及人口密度統計表 '])
a1=list(data['Unnamed: 6'])
for x in a :
    print(x)
print(a[3:28])
print(type(a))
plt.plot(a[3:28],a1[3:28])
plt.show()
