num1 = int(input("enter first number "))
num2 = int(input("enter second number "))
if num1==1:
    num1+=1
while True:
    for i in range(2,num1):
        if num1 % i == 0:
            break
    else:
        print(num1,end=" ")
    num1+=1
    if num1==num2:
        break