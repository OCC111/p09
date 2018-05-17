def add(a,b,c):   #定义一个函数名称
    return a+b+c   #

def pingjun(x,y,z):
    p = add(x,y,z) #变量g调用add函数，add赋值给g
    return p/3

g = add(20,20,20) #赋值给g，打印输出
#print(g)

p = pingjun(15,15,15) #赋值给p，打印输出
print(p)
