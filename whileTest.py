#循环 while
#whlie语句作用的范围是
#下方相同缩进的 所有语句
#while 循环条件：
#pass
#pass
#循环条件
#1.是否成立：True / False
#2.条件判断控制 a 比较 b

#===============================

#while True:
#    print("特大公益活动开始啦!")

#True:始终成立
#false：始终不成立

#-----------------------------
#qiandao = 1 #没有签到
#while qiandao:   
#    print("签到吧！%d" % qiandao) #  %d占位（随机出数）
#    qiandao = qiandao+2

#控制循环次数的三个关键点
#1.初始数值
#2.循环条件
#3.步长

a = 1
while a <= 1000:
    if a%2 == 2:
        print ("%d 是偶数" % a)
    else :
        print ("%d 是奇数" % a)
    a = a+2






























