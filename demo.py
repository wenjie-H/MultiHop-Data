import pandas as pd

# 读取.csv文件
df = pd.read_csv('460.csv')

# 遍历每一行数据
for index, row in df.iterrows():
    print(row)
