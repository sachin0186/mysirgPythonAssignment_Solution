n=int(input("enter a number "))
i=1
sum=0
while i<=n:
    sum=sum+i
    if i==10:
        print(i,"=",end=" ")
    else:
        print(i,"+",end=" ")
    i += 1
print(sum, end=" ")