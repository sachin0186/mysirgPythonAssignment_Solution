n=int(input("enter a number"))
sum = 0
i = 0
while i<=2*n:
    if i%2!=0:
        sum=sum+i
        if i==2*n-1:
            print(i,"=",end=" ")
        else:
            print(i,"+",end=" ")
    i+=1
print(sum)