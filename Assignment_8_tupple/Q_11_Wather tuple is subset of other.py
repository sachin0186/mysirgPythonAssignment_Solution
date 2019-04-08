a=eval(input("enter first  tuple value : "))
b=eval(input("enter second tuple value "))

for x in b :
    if x not in a  :
        print(b,"is not subset of ",a)
        break
else:
    print(b,"is subset of ",a)

