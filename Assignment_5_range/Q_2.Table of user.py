a=int(input("enter choiced table "))
print(a,"=",end=" ")
for i in range(a,10*a+1):
    if i%a==0:
        if i<a*10:
            print(i,end="*")
        else:
            print(i)