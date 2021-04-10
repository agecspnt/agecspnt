"""
3. 编写函数，模拟二分法查找。自主生成或者从键盘输入一个序列数据（不少于20个）放在列表中，
采用二分法从列表中查找一个数据，无论找到还是未找到都需要打印输出查找后的结果。
"""


def BinarySearch(ls, x, low, high):
    # 递归法实现二分查找
    if low <= high:
        mid = int((low + high) / 2)  # 强制转换int来消除小数点后面的数
        if ls[mid] == x:
            return mid  # 找到并返回其位置
        elif ls[mid] > x:
            return BinarySearch(ls, x, low, mid - 1)  # 左边
        else:
            return BinarySearch(ls, x, mid + 1, high)  # 右边
    else:
        return -1  # 未找到


def main():
    ls = [5, 7, 23, 34, 213, 675, 1243, 6456, 6564]
    print(ls)
    x = [1, 5, 213, 1243]
    for each in x:
        if BinarySearch(ls, each, 0, len(ls) - 1) == -1:
            print("未找到！！")
        else:
            print("已找到！其位置为：%d" % (BinarySearch(ls, each, 0, len(ls) - 1)))
        print()


if __name__ == '__main__':
    main()
