n=int(input("Enter the size of the array"))
lst=[]
for i in range(0,n+1):
    a=int(input("Enter any integer"))
    lst.append(a)
print(lst)
x=lst.count(2)
print(x)
lst.extend([23,89,42])
print(lst)
print(lst.index(0))
lst.remove(23)
print(lst)
