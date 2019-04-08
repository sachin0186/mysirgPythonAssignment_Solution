'''n=int(input("enter value of n to find list of n prime number"))
l=[]
count=0
i=2
while True:
    for x in range(2,i):
        if i%x==0:
            break
    else:
        l.append(i)
        count+=1
        if count==n:
           print(l)
           break
    i+=1
'''
n=int(input("enter a number"))
l=[]
x=2
while n:
   if all(x%i!=0 for i in range(2,x)):
       l+=[x]
       #l.append(x)
       n-=1
   x+=1
print(l)