import re
s = """Nowadays computers are widely used by not only adults but also children as the rapid development of the modern 
technology. I disagree that using computers has more negative effects on children. 

From my point of view, using computers in an early age could help young children cultivate their curiosity and 
practical skills in computering . As we all know,the Internet is multiple and complex,children will be attracted by 
its content and information. It is also positive for children to have their computer skills improved and develop the 
ability of accessing information which could be helpful for their future studies and working lives. Moreover,
children have the chances to vary their spare time by using computers. They could play online games,watch movies and 
even make new friends through the Internet. 

However, there are several disadvantages for children to use computers. Using computers may has a bad effect on 
children’s eyesight and may change their physical posture because it is unavoidable for them to sit in front of the 
computer for a long time. Otherwise,some computer games may cause children to form violent acts and preference. 
Sometimes there are too many violent factors in computer games which could mislead youngsters and cause imitation. 

To conclude, though playing computers in a young age is of a young age is negative sometimes,the benefits are 
obviously. Children should be self-discipline and play computers under the proper supervision of their parents. """

s = s.lower()  # 都转换成小写
s = re.sub('[,.\"-]', "", s)  # 用正则表达式去除所有标点符号
words = s.split()
print("文章中的单词总数：", len(words))
wordset = set(words)  # 利用集合去除重复的单词
print("去重后的单词总数：", len(wordset))

d = dict()
for i in wordset:
    d[i] = words.count(i)
print("词频统计结果如下：")
print(d)
