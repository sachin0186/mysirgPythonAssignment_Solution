
a=input("enter a word")
b=input("enter second word ")
c=input("enter three word")
if a>=b and a>=c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif a<=b and a<=c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
