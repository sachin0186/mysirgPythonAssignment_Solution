num=int(input("enter a number "))
x=num+1
while True:
    for i in range(2,x):
        if x%i==0:
            break
    else :
        print("the next prime number is ",x)
        break
    x+=1