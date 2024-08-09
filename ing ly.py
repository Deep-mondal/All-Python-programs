s = input("Enter your string")
l = len(s)
if (l >= 3):
    if (s[l-3] == 'i' and s[l-2] == 'n' and s[l-1] == 'g'):
        print(s+"ly")
    else:
        print(s+"ing")
else:
    print("System required more then 3 letter(You can add space)")
