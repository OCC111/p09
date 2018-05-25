list1=['1宫保鸡丁','2鱼香肉丝','3喜庆满堂六彩碟','4白花胶鸡煲汤','5秋油蒸深海石斑','6法式锦蔬焗扇贝']
print('☺ '*25)
print('   欢迎来到威妥码国际大酒店')
print('本店新开张，一周内所有业务免费')
print('        2.选择vip房间')
print('         3.菜品详情')
print('         4.********')
print('☺ '*25)

list2=[]
import time
    
def fangjian():
    dic1={}
    time.sleep(2)
    print('由于相关规定您需要先输入本人信息方可进入系统！')
    time.sleep(2)
    name = input('请输入您的姓名:')
    time.sleep(2)
    phone = int(input('请输入您的手机号:'))
    time.sleep(2)
    p_card = input('请出示您的身份证:')
    dic1['name']=name
    dic1['phone']=phone
    dic1['p_card']=p_card
    list2.append(dic1)
    time.sleep(2)
    print('客官，您的信息添加成功！！！')
    time.sleep(2)
    print('您输入的信息是：',list2)
fangjian()
while True:
    import random
    vip=random.randint(666001,666999)
    time.sleep(2)
    fang = input('请您选择要进入的程序:')
    if fang == '2':
        time.sleep(2)
        print('欢迎进入vip房间%d'% vip)
    elif fang == '3':
        time.sleep(4)
        for i in list1:
            time.sleep(2)
            print('-'*30)
            print(list1[0])
            print(list1[1])
            print(list1[2])
            print(list1[3])
            print(list1[4])
            print(list1[5])
            print('-'*30)
            time.sleep(2)
            pinming = input('请输入菜品编号:')
            if pinming == '1':
                time.sleep(3)
                print('已选定-宫保鸡丁-请您稍等...')
                time.sleep(5)
                print('客官，您的菜来喽！请您慢用！！') 
                time.sleep(5) 
            elif pinming == '2':
                time.sleep(5)
                print('已选定-鱼香肉丝-请您稍等...')
                time.sleep(5)
                print('客官，您的菜来喽！请您慢用！！') 
                time.sleep(5)
            elif pinming == '3':
                print('已选定-喜庆满堂六彩碟-请您稍等...')
                time.sleep(5)
                print('客官，您的菜来喽！请您慢用！！') 
                time.sleep(5)
            else:
                time.sleep(5)
                print('您输入有误，正在退出系统中...')
                break
    elif fang == '4':
        time.sleep(3)
        print('即将进入后台系统...') 
        time.sleep(3)
        print('不要着急，已经很努力的加载啦...') 
        time.sleep(3)
        print('正在做最最最后的处理...') 
        time.sleep(6)
        print('亲爱的威妥玛，欢迎您进入后台系统☺')
        time.sleep(3)
        print('   ')
       

        jiang=['恭喜您中奖，接下来只需要您打开手机微信转发这条消息到100个群里，账户就会有100元，并且会有威妥玛国际大酒店总经理的亲笔签名照一张']
        for i in jiang:
            print(i)



            
    else :
        time.sleep(3)
        print('请您立刻马上退出系统，否则后果自负！！！')
        break    

