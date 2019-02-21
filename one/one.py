phone = input("请输入手机号：")
list = [185,137,136,176,151,153]
try:
    #判断是否是纯数字
    int(phone)
    #判断手机号长度
    if(len(phone) == 11):
        #通过异常判断手机号是否为数字
        head = phone[0:3]
        bool = False
        for i in list:
            if(int(head) == i):
                bool = True
                break
        if(bool):
            print("有效手机号")
        else:
            print("无效手机号")
    else:
        print("输入的不是有效手机号")
#       手机号码不为数字
except ValueError:
    print("输入的不是有效手机号")
