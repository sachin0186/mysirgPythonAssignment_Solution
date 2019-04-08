num=int(input("enter number "))
if num==2:
    print("prime")
elif num==0 or num==1:
    print(" neither prime nor composite")
else :
    for x in range(2,num):
        if num%x==0:
            break
    if x==num-1:
        print("prime number ")
    else:
        print("not prime number ")