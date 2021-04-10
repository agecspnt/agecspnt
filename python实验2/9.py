"""
9.输入一个大于2的自然数，输出小于该数字的所有素数组成的集合。
"""


def isPrime(x):
    if x == 1:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1


x = int(input())
s1 = set()
for i in range(1, x):
    if isPrime(i) == 1:
        s1.add(i)
print(s1)
