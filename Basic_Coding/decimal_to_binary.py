num = 15

print(bin(num))   # using built-in method

def check(num):
    binary = 0
    place = 1

    while num>0:
        rem = num%2
        binary+=rem*place
        place*=10
        num = num//2

    print(binary)

check(num)