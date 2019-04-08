a=float(input("enter the coefficient of x^2"))
b=float(input("enter the coefficient of x"))
c=float(input("enter the constant term"))
d=(b**2)-(4*a*c)
print("d = ",d)
if d>0:
    root_1=(-b+d**0.5)/2*a
    root_2=(-b-d**0.5)/2*a
    print("roots are real and dinistict",root_1,"and",root_2)
elif d==0:
    root_1 = ((-b) + (d ** 0.5)) / 2 * a
    print("roots are real and same", root_1)
else:
    print("roots are imagenary")
