'''def prime(num):
    half=num//2
    for i in range(1,half+1):
        if(num%i==0.0):
            return
        else:
            return num'''
low=int(input("Enter the lower boundery:"))
up=int(input("Enter the higher boundery:"))
for i in range(low,up+1):
  half=i//2
  if (i==1):
    print(i)
  elif(i==2):
    print(i)
  else:
    for j in range(2,half+1):
        if(i%j==0):
             break
        else:
            print(i)