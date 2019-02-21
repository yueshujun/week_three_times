import random
list = []
#生成一个包含50个随机整数的列表，随机整数的范围是从-10到10
for i in range(50):
    num = random.choice(range(-10,11))
    list.append(num)

print("list长度：",len(list))

zheng = []
fu = []
#遍历列表区分正负数
for i in list:
    if (i>0):
        zheng.append(i)
    else:
        fu.append(i)
print("正数：",zheng)
print("负数；",fu)










