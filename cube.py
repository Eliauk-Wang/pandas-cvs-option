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



运行结果：
(68921, 4)
[[  0   0  30 186]
 [  0   0  31 192]
 [  0   0  32 198]
 [  0   0  33 204]
 [  0   0  34 210]
 [  0   0  35 216]
 [  0   0  36 222]
 [  0   0  37 228]
 [  0   0  38 234]
 [  0   0  39 240]]
行： [  0   0  33 204]
列 [30 31 32 33 34 35 36 37 38 39]
