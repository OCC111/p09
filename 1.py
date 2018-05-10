def check_age(age):
    if age > 0 and age < 5:
        print ("婴孩")
    elif age > 5 and age < 10:
        print ("见习")
    elif age > 10 and age < 18:
        print ("青年")
    elif age > 18 and age < 30:
        print ("成年人")
    elif age > 30 and age < 50:
        print ("中年人")
    elif age > 50 and age < 80:
        print ("老年人")
    elif age > 80 and age < 200:
        print ("寿星")
    elif age >=200:
        print ("妖精")
age = int(input("请输入您的年龄:"))
check_age(age)
