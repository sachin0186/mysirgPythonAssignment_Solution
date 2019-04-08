n=int(input("enter a number "))
z=n
x=2
while x<=n:
    for y in range(2,x):
        if x%y==0:
            x+=1
            break
    else:
        if n%x==0:
            print(x,end=" ")
            n=n/x
        else:
            x+=1
