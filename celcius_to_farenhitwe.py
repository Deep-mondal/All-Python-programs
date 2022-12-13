print("1.C to F\
      2.F to C")
a = int(input("Enter your Choice by a number"))
if (a == 1):
    c = float(input("Enter the tempareture"))
    f = ((9/5)*c)+32
    print(f)
elif (a == 2):
    f = float(input("Enter the tempareture"))
    c = (5/9)*(f-32)
    print(c)
else:
    print("Invalid Entry")
