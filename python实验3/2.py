"""
2. 编写函数，模拟选择法排序。自主生成或者从键盘输入需要排序的序列数据（不少于20个）放在列表中，
采用顺序排序，并打印输出排序后的结果。
"""


def selection_sort(ls):
    # 选择排序
    min_index = 0  # 初始化
    for j in range(len(ls) - 1):  # 外层循环
        min_index = j
        for i in range(j + 1, len(ls)):  # 内层循环
            if ls[min_index] > ls[i]:
                min_index = i
        print(min_index)
        ls[j], ls[min_index] = ls[min_index], ls[j]  # 将最小值与当前循环的首位交换
    print(ls)


def main():
    # 主函数
    ls = [2, 1, 3, 5, 6, 4]
    selection_sort(ls)


if __name__ == '__main__':
    main()
