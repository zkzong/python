import pandas as pd

path = 'file/example.csv'

csv = pd.read_csv(path)
print(csv)

# 如何指定字符集类型 encoding=None
csv = pd.read_csv(path, encoding="utf8")
print(csv)

# 如何指定表头/列名行 header=0
pd.read_csv(path, header=1)

# 如何指定分隔符 sep=","
pd.read_csv(path, sep='/')

# 如何自定义列名 names=None
pd.read_csv(path, names=['ts_code', 'symbol', 'name', 'area', 'industry', 'list_date'])

# 如何指定行索引 index_col=None
pd.read_csv(path, index_col="ts_code")

# 如何读入指定列数据 usecols=None
pd.read_csv(path, usecols=["ts_code", "area"])

# 如何读入前N行数据 nrows=None
pd.read_csv(path, nrows=2)

# 如何跳过前N行数据 skiprows=None
pd.read_csv(path, skiprows=2)

# 如何指定数据类型 dtype=None
pd.read_csv(path, dtype={"list_date": "str"}).info()

# 如何读入时进行数据运算 converters=None
pd.read_csv(path, converters={"ts_code": lambda code: code[:6]})

# 如何读入时对日期时间列进行转换 parse_dates=False
pd.read_csv(path, parse_dates=["list_date"])
