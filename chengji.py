def check_cj(cj):
    if cj > 60 and cj < 80:
        print ("合格")
    elif cj > 80 and cj < 95:
        print ("优秀")
    elif cj > 95 :
        print ("SSS+")
    else :
        print ("老铁重学吧!")
cj = int(input("输入成绩了您呐:"))
check_cj(cj)

# p09
