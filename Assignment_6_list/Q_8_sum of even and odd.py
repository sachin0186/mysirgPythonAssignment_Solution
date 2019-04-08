l=[int(x) for x in input("enter number seprated by ',': ").split(",")]
sumeven=0
sumodd=0
for e in l:
    if e%2==0:
        sumeven+=e
    else:
        sumodd+=e
print("sum of even all even in list is -",sumeven,"\n","sum of all odd in given list is --",sumodd)