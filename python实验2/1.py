"""1.编写程序，从键盘输入任意大的自然数，然后打印输出各位数字之和。"""
x = input()
Sum = 0
for i in x:
    Sum += int(i)
print(Sum)
