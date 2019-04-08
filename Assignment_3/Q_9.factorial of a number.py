n=int(input("enter a number "))
product=1
i=n
while i>=1:
    product=product*i
    if i==1:
        print(i,"=",end=" ")
    else:
        print(i,"*",end=" ")
    i-=1
print(product)