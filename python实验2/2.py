"""2.编写程序， 首先自主创建两个集合SetA和SetB，然后分别输出它们的交集、并集、差集（SetA-SetB）和补集。（要求用两种方法解题）。"""

"""第一种方法"""
SetA = {'a', 'b', 'c', 'd', 'e'}
SetB = {'c', 'd', 'e', 'f', 'g'}
print(SetA & SetB)  # 交集
print(SetA | SetB)  # 并集
print(SetA - SetB)  # 差集
print(SetA ^ SetB)  # 补集

print()

"""第二种方法"""
SetC = {'a', 'b', 'c', 'd', 'e'}
SetD = {'c', 'd', 'e', 'f', 'g'}
print(SetC.intersection(SetD))
print(SetC.union(SetD))
print(SetC.difference(SetD))
print(SetC.symmetric_difference(SetD))


