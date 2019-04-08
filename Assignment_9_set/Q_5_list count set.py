print("enter list value seperated by comma")
l=[eval(x) for x in input().split(",")]
s=set(l)
print("the total number of distinct element in list is ",len(s))