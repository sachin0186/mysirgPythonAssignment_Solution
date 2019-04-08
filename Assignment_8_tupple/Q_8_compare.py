a=eval(input("enter first tuple value : "))
b=eval(input("enter second tuple value : "))
if len(a)==len(b):
    for x in a:
        if x not in b:
            print("tuples are not equal")
            break
    else:
        print("the tuples are equal")

