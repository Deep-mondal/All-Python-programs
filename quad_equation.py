a=int(input("Put the coefficient of x^2"))
b=int(input("Enter The coefficient of x"))
c=int(input("Enter the constant term"))
f=b**2-(4*a*c)
if(f>=0):
    r1=(-b+(b**2-(4*a*c)))/2*a
    r2=(-b-(b**2-(4*a*c)))/2*a
    print("Thye roots are",r1,r2)
else:
    r1=(-b+(b**2-(4*a*c)))/2*a
    r2=(-b-(b**2-(4*a*c)))/2*a
    x=complex(r1)
    y=complex(r2)
    print("The roots are",x,y)