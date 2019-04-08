num=int(input("enter numer "))
s=set()
x=2
count=0
while True:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        s.add(x)
        count+=1
        if count==num:
            break
    x+=1
print(s)