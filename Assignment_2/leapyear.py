year=int(input("enter the year"))
if year%400==0:
    print("leap year")
elif year%100==0:
    new_year=year/100
    if new_year%4==0:
        print("leap year0")
    else:
        print("not leap year ")
elif year%4==0 and year%100!=0:
    print("leap yaer")
else:
    print("not leap year")