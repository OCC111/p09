import datetime
count = 0
while count < 3:
    username = input("username:")
    pwd = input("passwd:")
    dayT = datetime.date.today()
    if username.strip()=="" or pwd.strip()=="":
        print("your input is null,please input again!")
        count += 1
        continue
    elif username == "wtm" and pwd == "123456":
        print("%s,欢迎登录，今天的日期是：%s,程序结束"%(username,dayT))
        break
    else:
        print("you have tried 3times,the user has been locked!")
