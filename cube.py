import pandas as pd
import numpy as np
data_set = []
for i in range(41):
    for j in range(41):
        for k in range(41):
            if i > 10 and i < 32 and j > 10 and j < 32:
                data_set.append([1 * i, 1 * j, 1 * k, 12 * (k + 1)])
            else:
                data_set.append([1 * i, 1 * j, 1 * k, 6 * (k + 1)])
Coordinates = pd.DataFrame(np.mat(data_set))
headers=['x','y','x','B']
#数据存储到csv
Coordinates.to_csv("cube.csv", header=headers, index=0)
#读取csv文件
data=pd.read_csv("cube.csv")
print(data.shape)
#读取某一段数据
d=data.values[list(range(30, 40))]
print(d)
#打印某一行
print("行：",d[3])
#打印某一列
print("列",d[:,2])
