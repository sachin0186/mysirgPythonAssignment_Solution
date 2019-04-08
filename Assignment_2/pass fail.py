sub_name_1=int(input("enter your ADA marks "))
if sub_name_1>100 or sub_name_1<0:
    print("invalid marks: the marks should be in between 0 to 100")
else:
    sub_name_2=int(input("enter your DS Marks "))
    if sub_name_2 > 100 or sub_name_1 < 0:
        print("invalid marks: the marks should be in between 0 to 100")
    else:
        sub_name_3=int(input("enter your OS marks  "))
        if sub_name_3 > 100 or sub_name_1 < 0:
            print("invalid marks: the marks should be in between 0 to 100")
        else:
            sub_name_4=int(input("enter your SE marks  "))
            if sub_name_1 > 100 or sub_name_1 < 0:
                print("invalid marks: the marks should be in between 0 to 100")
            else:
                sub_name_5=int(input("enter your CSO marks  "))
                if sub_name_1 > 100 or sub_name_1 < 0:
                    print("invalid marks: the marks should be in between 0 to 100")
total_sub=sub_name_1+sub_name_2+sub_name_3+sub_name_4+sub_name_5
percent=(total_sub/500)*100
print("sub \t marks \t pass/fail")
if sub_name_1>=30:
    print("ADA \t ",sub_name_1," \t pass")
else:
    print("ADA \t ", sub_name_1, " \t fail")
if sub_name_2>=30:
    print("DS  \t ",sub_name_2," \t pass")
else:
    print("DS  \t ", sub_name_2, " \t fail")
if sub_name_3>=30:
    print("OS  \t ",sub_name_3," \t pass")
else:
    print("OS  \t ", sub_name_3, " \t fail")
if sub_name_4>=30:
    print("SE  \t ",sub_name_4," \t pass")
else:
    print("SE  \t ", sub_name_4, " \t fail")
if sub_name_5>=30:
    print("CSO \t ",sub_name_5," \t pass")
else:
    print("CSO \t ", sub_name_5, " \t fail")
if percent>30 and sub_name_1>=30 and sub_name_2>=30 and sub_name_3>=30 and sub_name_4>=30 and sub_name_5>=30:
    print("----------------------")
    print("total: \t ",total_sub," \t pass")
    print("percentage: ",round(percent,2),"%")
    if 30<=percent<40:
        print("grade : D")
    elif 40<=percent<50:
        print("grade: C")
    elif 50 <= percent < 60:
        print("grade: B")
    elif 60 <= percent < 70:
        print("grade: A")
    elif 70 <= percent < 80:
        print("grade: A+")
    elif 80<=percent<90:
        print("grade : A++")
    elif 90 <= percent < 100:
        print("grade:  Congrats!! Outstanding!! You beat the highest grade A+++")
else:
    print("total: \t ", total_sub, " \t fail")