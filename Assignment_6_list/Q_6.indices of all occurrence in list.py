'''l=[eval(e) for e in input("enter a numbner seprated by',': ").split(",")]
e=eval(input("enter the value you want to search "))
index=0
for i in range(0,len(l)):
    if l[i]==e:
        print(i,end=" ")
'''
l=[eval(e) for e in input("enter a numbner seprated by',': ").split(",")]
e=eval(input("enter the value you want to search "))
index=0
while index<len(l):
    if l[index]==e:
        print(index,end=" ")
    index+=1