y=int(input("Enter the Year to be checked"))
if(y%400==0 and y%100==0):
    print("It is a leap year")
elif(y%4==0 and y%100!=0):
    print("It is a leap year")
else:
    print("It is not a  leap year")
