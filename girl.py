def check_age(age):    
    if age > 0 and age < 2:
        print ("婴儿")
    elif age >= 3 and age < 7:
        print ("儿童")
    elif age >= 8 and age < 12:
        print ("见习者")
    elif age >= 13 and age < 30:
    	print ("成年人")
    elif age >= 31 and age < 40:
        print ("奋斗期")
    else :
        print ("长辈")
age = int(input("请输入您的年龄:"))
check_age(age)
 
