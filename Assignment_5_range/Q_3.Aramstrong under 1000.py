i=0
while i<=1000:
        n=i
        sum=0
        while n>0:
            r=n%10
            n=n//10
            sum=sum+r**3
        if i==sum:
            print(sum,end=" ")
        i+=1