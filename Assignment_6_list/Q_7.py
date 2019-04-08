'''l=[eval(x) for x in input("enter number seperated by ',' : ").split(",")]
set=set(l)
for e in set:
    count=0
    index=0
    while index<len(l):
        if l[index]==e:
            count+=1
        index+=1
    print(e, "-", count)
'''
l=[int(x) for x in input("enter number seperated by ',' : ").split(",")]
i=0
for e in l:
    if l.index(e)==i:
        print(e,"--",l.count(e))
    i+=1