'''s=input("enter string ")
e=input("enter the element you want to search")
for i in s:
    if i==e:
        print(e,"--",s.count(i))
        break
'''
#programs to count occurrence of all elements in string
a=input("enter string ")
y=0
for i in a:
    if a.index(i)==y:
        print(i,"--",a.count(i))
        y+=1