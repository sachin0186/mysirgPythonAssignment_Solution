num_1=int(input("enter first number "))
num_2=int(input("enter second number "))

for i in range(2,num_2):
    if num_1%i==0 and num_2%i==0:
        print("not co-prime")
        break
else:
    print("co-prime ")
