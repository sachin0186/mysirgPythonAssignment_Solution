a=int(input("enter starting value"))
b=int(input("enter stop value"))
c=int(input("enter step value"))
if b>a and c>0 or b<a and c<0:
    for i in range(a,b+1,c):
            print(i,end=" ")
else:
    print("invalid output")