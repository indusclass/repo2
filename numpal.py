num=int(input("Enter number:"))
temp=num
revnum=0
while temp!=0:
    rem=temp%10
    temp=temp//10
    revnum=revnum*10+rem

if num==revnum:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


