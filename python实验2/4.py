"""
4.编写程序，自主构建一个整数列表，然后输出列表中所有整数连乘的结果。
"""
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Sum = 1
for i in ls:
    Sum *= i
print(Sum)
