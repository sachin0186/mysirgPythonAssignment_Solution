m=int(input("enter month in numeric notation: "))
l_1=[1,3,5,7,8,10,12]#list of 31 days months
l_2=[2,4,6,9,11]
if m==2:
    year = int(input("enter the year"))
    if year % 400 == 0:
        print("this is a leap year so the days in month",m,"is","29")
    elif year % 100 == 0:
        new_year = year / 100
        if new_year % 4 == 0:
            print("this is a leap year so the days in month", m, "is", "29")
        else:
            print("this is not a leap year so the days in month ",m,"is 28")
    elif year % 4 == 0 and year % 100 != 0:
        print("this is a leap year so the days in month", m, "is", "29")
    else:
        print("this is not a leap year so the days in month ", m, "is 28")
elif m in l_1:
    print("number of days in month ", m, " is", "31")
elif m in l_2:
    print("number of days in month ", m, " is", "30 ")
else:
    print("you have entered an invalid month")