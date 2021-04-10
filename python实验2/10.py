"""
10.使用枚举法验证6174猜想：1955年，卡普耶卡对4位数字进行了研究，发现一个规律：
对任意各位数字不相同的4位数，使用各位数字能组成的最大数减去能组成的最小数，对得到的差重复这个操作，
最终会得到6174这个数字，并且这个操作不会超过7次。要求：使用枚举法对这个猜想进行验证。
"""


def divideDigit(x):
    ls = [int(i) for i in str(x)]
    return ls


def createDigit(ls):
    res = ls[0] * 1000 + ls[1] * 100 + ls[2] * 10 + ls[3]
    return res


def subtractDigit(ls):
    ls.sort()
    min_digit = createDigit(ls)
    ls.sort(reverse=True)
    max_digit = createDigit(ls)
    res = max_digit - min_digit
    return res


def verify(ls):
    res = 0
    cnt = 0
    flag = 1
    createDigit(ls)
    while res != 6174:
        res = subtractDigit(ls)
        ls = [int(i) for i in str(res)]
        cnt += 1
    if cnt > 7:
        print("验证失败")
        flag = 0
    if flag == 1:
        return 1


def main():
    x = 0
    for i in range(1000, 10000):
        ls = divideDigit(i)
        if ls[0] != ls[1] and ls[0] != ls[2] and ls[0] != ls[3] and ls[1] != ls[2] and ls[1] != ls[3] and ls[2] != ls[
            3]:
            x = verify(ls)
    if x == 1:
        print("验证成功,所有操作次数均小于7次")


if __name__ == '__main__':
    main()
