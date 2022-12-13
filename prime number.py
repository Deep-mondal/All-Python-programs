num = int(input("Enter a number:"))
half = num//2
c = 0
if (num == 1):
    print("It is a prime number")
elif (num == 2):
    print("It is a prime number:")
else:
    for i in range(2, half+1):
        if (num % i == 0.0):
            c = c+1
if (c == 0):
    print("It a Prime number")
else:
    print("It is not a prime number")
