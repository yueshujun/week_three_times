import random
str = 'abcd'
str1 = ''
#随机生成一个包含1000个字母的字符串
for i in range(1000):
    str += random.choice(str)
print("字符串的长度：",len(str1))

dict = {}
for i in str1:
    key = dict.get(i)
    #每个字母的数量
    if (key == None):
        dict[i] = 1
    else:
        dict[i] += 1
#输出结果
print(dict)