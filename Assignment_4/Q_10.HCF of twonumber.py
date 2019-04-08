num1=int(input("enter first no "))
num2=int(input("enter second no "))
a=min(num1,num2)
while a>=1:
    if num1%a==0 and num2%a==0:
        print("HCF is ",a)
        break
    a-=1