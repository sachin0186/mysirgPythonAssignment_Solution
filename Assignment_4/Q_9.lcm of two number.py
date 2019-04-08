num_1=int(input("enter first no "))
num_2=int(input("enter second no. "))
max=max(num_1,num_2)
for x in range(max,num_1*num_2):
    if x%num_1==0 and x%num_2==0:
        print("lcm of ",num_1 ,"and",num_2,"is",x)
        break