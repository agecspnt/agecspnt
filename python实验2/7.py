"""
7.编写程序，按照如下步骤：
（1）分别创建2个包含若干元素且长度不同的列表，并打印输出2个列表；
（2）使用第（1）步创建的2个列表来创建1个字典；
（3）计算并输出字典长度；
（4）打印输出整个字典；
（5）输出该字典中一个一个的元素对。
"""

ls1 = [1, 2, 3, 4, 5, 6]
ls2 = ['a', 's', 'd', 'f', 'g', 'h', 'j']
d = zip(ls1, ls2)
d = dict(d)
print('字典长度:', len(d))
print(d)
for each in d.items():
    print(each)
