'''a=input("enter string: ")
y=0
for e in a:
    if a.index(e)==y:
        print(e,end="")
        y+=1

'''
a=[input(" enter name ") for x in range(int(input("enter the no of names you want to enter")))]
#print(a)
b=set(a)
a=list(b)
for x in b:
    print(x)