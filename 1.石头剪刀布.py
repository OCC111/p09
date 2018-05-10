import random 
while True:
    pc = random.randint (1,3)
    wtm = int(input("请出拳,1石头，2剪刀，3布"))
    if pc == 1:
        print("电脑：石头")
    elif pc == 2:
        print("电脑：剪刀")
    else :
        print("电脑：布")
    if wtm == 1:
        print("钻石级玩家:石头")
    elif wtm == 2:
        print("钻石级玩家:剪刀")
    else :
        print("钻石级玩家:布")
    if (wtm == 1 and pc == 2) or (wtm == 2 and pc == 3) or (wtm == 3 and pc == 1):
        print("钻石级玩家：电脑弱爆了！！")
    elif (wtm == 1 and pc == 3) or (wtm == 3 and pc == 2) or (wtm == 2 and pc == 1):
        print("电脑：加油哦！不过你是不会赢我的")
    else :
        print("电脑：心有灵犀，再来一次吧!")
