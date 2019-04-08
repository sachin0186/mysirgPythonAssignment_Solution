'''l=[int(x) for x in input("enter number seprated by ',' ").split(",")]
m=sum(l)
print(m)
'''

l=[int(x) for x in input("enter number seprated by ',' ").split(",")]
sum=0
for i in l:
    sum+=i
print(sum)
