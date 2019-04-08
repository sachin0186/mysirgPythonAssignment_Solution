m=int(input("enter month in numeric notation: "))
if m==2:
        print("number of days in month ",m," is","28 for normal year and 29 for leap year ")
elif 1 <= m <= 7:
        if m%2==0:
            print("number of days in month ",m," is","30")
        else:
            print("number of days in month ",m," is","31")
elif 8<=m<=12:
    if m%2==0:
        print("number of days in month ", m, " is", "31")
    else :
        print("number of days in month ", m, " is", "30")
else:
    print("you have entered an invalid month")

