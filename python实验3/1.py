"""
1. 编写函数，查找序列元素的最大值和最小值。从键盘得到一个序列，返回并打印输出一个元组，
其中元组第一个元素为序列最大值，第二个元素为序列最小值。
"""


def demo(ls):
    # 查找序列元素的最大值和最小值并以元祖形式返回
    return max(ls), min(ls)


def main():
    # 主函数
    ls = list(eval(input()))  # 输入一个序列，自动识别并转换为列表
    print(demo(ls))


if __name__ == '__main__':
    main()
