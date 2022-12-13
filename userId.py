def creat():
    a = input("Enter the name:")
    b = int(input("Enter the current year"))
    return a, b


def getChar():
    a = input("Do you want to continue")
    return a


def menu():
    print("***********")
    print("  "+"Menu"+"  ")
    print("***********")
    print("1.Creat ID")
    print("2.Display")


def idMaker():
    id = []
    i = 1
    while (1):
        menu()
        ch = int(input("Enter a choice by a number:"))
        if (ch == 1):
            x, y = creat()
            a = len(x)
            p = x[0:2]
            b = y % 100
            d = 1008, b, p, a, i
            id.append(d)
            i = i+1
        elif (ch == 2):
            print(id)
        else:
            print("Invalid Choice Number please give the right choice no and try again!")
        r = getChar()
        while (r != 'y' or r != 'Y'):
            break


idMaker()
