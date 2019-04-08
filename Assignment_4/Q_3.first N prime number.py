'''num=int(input("enter n number to get n number of prime number  : "))
k=0
j=2
while True:
    for i in range(2,j):
        if j%i==0:
            break
    else:
        k+=1
        print(j,end=" ")
    j+=1
    if k==num:
        break
        '''
num = int(input("enter : "))
while num==0:
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
    num-=1
