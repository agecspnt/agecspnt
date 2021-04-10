"""
8.编写程序，创建一个字符串，输出其中出现次数最多的字符及其出现的次数，要求使用字典。（欢迎用多种方法实现）
"""
s = 'dadadcdgtrbytadvgfbgrrthfiuenvocosmco'
d1 = {}
for each in s:
    if each not in d1:
        d1.setdefault(each, 1)
    else:
        d1[each] += 1
TempList = sorted(d1.items(), key=lambda x: x[1], reverse=True)
print('出现次数最多的字符:', TempList[0][0])
print('其出现次数为:', TempList[0][1])
