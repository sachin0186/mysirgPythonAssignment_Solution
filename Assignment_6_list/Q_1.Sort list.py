a=[eval(x) for x in input("enter ").split()]
b=sorted(a)  #sorted() function return a list that is sorted
print(b)
a.sort() #but sort() function sort the list itself
print(a)