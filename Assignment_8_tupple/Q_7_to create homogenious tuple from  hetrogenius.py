a=eval(input("enter tuple value seperated by comma"))
b=[]
c=[]
d=[]
for x in a:
    if type(x)==int:
        b.append(x)
    elif type(x)==str:
        c.append(x)
    elif type(x)==float:
        d.append(x)
print(tuple(b))
print(tuple(c))
print(tuple(d))