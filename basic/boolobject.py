# author: zong
# date: 2022/4/20 22:12

# 测试对象的布尔值
print('----------------以下对象的布尔值为False-----------------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) # 空列表
print(bool(list())) # 空列表
print(bool(())) # 空元组
print(bool(tuple())) # 空元组
print(bool({})) # 空字典
print(bool(dict())) # 空字典
print(bool(set())) # 空集合

print('----------------其它对象的布尔值为True-----------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))