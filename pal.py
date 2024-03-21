st=input("Enter the string:")

pal=True
h=len(st)//2
for i in range (0,h):
    if st[i]!=st[-i-1]:
        pal=False
if pal:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
print("Changed")
