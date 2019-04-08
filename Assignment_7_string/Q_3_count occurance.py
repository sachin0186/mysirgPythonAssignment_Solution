l=input("enter a string ")
y=0
for e in l:
    if l.index(e)==y:
        y+=1
        print(e,'---',l.count(e))