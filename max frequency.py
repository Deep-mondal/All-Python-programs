s = input("Enter a string")
t = input("Enter your test charecter")
c = 0
j = 0
for i in s:
    if (t == s[j]):
        c = c+1
    j = j+1
print("The fequency of"+t, c)
