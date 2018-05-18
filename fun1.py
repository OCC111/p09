x = 1  #赋值给变量x
def fun1(*fun2): #定义一个函数名称
    global x#全局变量，当x在函数以外的时候必须加global
    for i in fun2:#
        x = x*i#
    print(x)#输出变量x的值
fun1(1,2,3,4,5,6,7,8,9)#调用函数fun1
