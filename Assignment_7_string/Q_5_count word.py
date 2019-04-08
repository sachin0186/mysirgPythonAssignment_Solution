'''s=input("enter string ").strip()
count=1
for i in range(0,len(s)-1):
    if s[i]==" " and s[i+1]!=" ":
        count+=1
print(count)
'''
'''
a=[x for x in input("enter ").split()]
print("there are" ,len(a),"words in the given string",)
'''

s=input("enter string ").strip()
count=1
i=0
for e in s:
    if s[i]==" " and s[i+1]!=" ":
        count+=1
    i+=1
print(count)
