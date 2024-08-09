lst = []
lst2 = []
for i in range(0, 5):
    a = int(input("Enter your element"))
    b = a in lst
    if (b == False):
        lst.append(a)
    else:
        print("Exist")
print(lst)
lst2 = lst
c = max(lst2)
lst2.remove(c)
print(max(lst2))
