'''n=int(input("enter number"))
l=[]
for i in range(1,n+1):
    s=i**2
    l=l+[s]
print(l)
'''
l= [ e**2 for e in range(1,int(input("enter number"))+1)]
print(l)