 num_1=int(input("enter the first number "))
num_2=int(input("enter the second number"))
num_3=int(input("enter the third number "))
if num_1>num_2:
    if num_1>num_3:
        print("the greater number is",num_1)
    else:
        print("the greater number is ",num_3)
elif num_1==num_2==num_3:
    print("all numbers are equal")
else:
    if num_2>num_3:
        print("the greate number is ",num_2)
    else:
        print("the greater number is ",num_3)
