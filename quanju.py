list_card = ['zhangsan',22,'nv']
a = 100
def test1():
    global a 
    a += 1
    print(a)
    c = 1
    list_card[2] = 'nan'  #此为更改对应的下标内容
    list_card.append('001')
    print(list_card) #打印输出 第一行列表中的内容
def test2():
    print(a)
test1()
test2()

