s=input("enter string to count vowel")
count=0
v="aeiouAEIOU"
for x in s:
    if x in v:
        count+=1
print("there ara ",count,"vowel in",s)