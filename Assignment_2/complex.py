c=complex(input("enter a complex number"))
if c.real>c.imag:
    print("the greater part is real i.e ",c.real)
elif c.real==c.imag:
    print("both are equal")
else:
    print("the imagenary part is greater i.e",c.imag)