"""
3.编写程序，首先自主创建两个长度不同的列表并打印输出，然后对这个列表进行排序，
一个升序，另一个降序，最后根据排序后的两个列表创建一个字典并输出该字典。
"""
ls1 = [3, 2, 1, 4, 5]
ls2 = [6, 4, 2, 8, 10, 100]
print(ls1, ls2)
ls1.sort()  # 升序
ls2.sort(reverse=True)  # 降序
x = {}  # 创建空字典
x = zip(ls1, ls2)
print(dict(x))

