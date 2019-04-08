print(" enter set value seperated by power ")
s={eval(x) for x in input().split(",")}
n=len(s)
new_s=set()
c=1
while c<= 2**n:
    for x in s:

        new_s.add(x)

    c+=1
print(new_s)