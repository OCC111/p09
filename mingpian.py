list1=['1宫保鸡丁','2鱼香肉丝','3喜庆满堂六彩碟','4白花胶鸡煲汤','5秋油蒸深海石斑','6法式锦蔬焗扇贝']
print('>'*25)
print('欢迎来到威妥码国际大酒店')
print('1.选择vip房间')
print('2.菜品详情')
print('3.查询对应的房间号')
print('>'*25)
import time
while True:
    fang = input('请选择菜单类型')
    if fang == '1':
        print('欢迎进入vip房间')
    else :
        print('后会有期，来日相见')
        break
    time.sleep(2)
    cai = input('选菜了您呐！！！')
    if cai == '2':
        time.sleep(2)
        print(list1)
        time.sleep(2)
        pinming = input('请输入菜品:')
        if pinming == '1':
            time.sleep(10)
            print('已选定-宫保鸡丁-请您稍等...')
            time.sleep(20)
            print('客官，您的菜来喽！请您慢用！！') 
