num = int(input("Enter Number"))
temp = num
def reverse_number(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    print(rev)

    if temp==rev:
        print("Palindrome")
    else:
        print("Not palindrome")

reverse_number(num)