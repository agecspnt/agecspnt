"""
4. 编写函数，模拟快速排序算法。自主生成或者从键盘输入需要排序的序列数据（不少于20个）放在列表中，
采用逆序排序，并打印输出排序后的结果。
"""


def quick_sort(array):
    less = []
    greater = []

    if len(array) <= 1:  # 递归结束判断
        return array

    pivot = array.pop()  # 利用pop()特性随机选取一个基准值

    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + [pivot] + quick_sort(greater)  # 递归


def main():
    ls = [2, 4, 2, 6, 7, 8, 1, 123, 435, 23,
          343, 1325435, 432, 1, 35, 6, 7, 8, 3, 2]
    print('排序前的列表为：', ls)
    print('排序后的列表为：', quick_sort(ls))


if __name__ == '__main__':
    main()
