a=eval(input("enter tuple value seperated by comma : "))
y=0
for x in a:
    if a.index(x)==y:
        print(x,"--",a.count(x))
    y+=1