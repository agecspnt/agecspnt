import random as r
"""
5.你会编写程序计算圆周率吗？查找资料学习蒙特·卡罗方法（通过概率统计得到问题近似解的方法），然后编写程序求解并打印输出圆周率。
"""
"""
思路：通过一个四分之一的圆和边长等于圆半径的正方形，随机在该图形上撒下‘小点’，最终通过圆内的’小点‘与圆外的’小点‘进行简单运算得出pi的取值。
"""

points = 0
for i in range(1000 ** 2):
    x, y = r.randint(0, 1000), r.randint(0, 1000)
    distance = pow(x ** 2 + y ** 2, 0.5)
    if distance <= 1000:
        points += 1
pi = 4 * (points / 1000 ** 2)
print(pi)


