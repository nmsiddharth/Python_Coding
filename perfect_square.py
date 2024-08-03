# (A perfect square is a positive integer that is obtained by multiplying an integer by itself)

import math

num = int(input("Enter Number"))

def perfect_number(num):
        root = math.isqrt(num)
        if root*root==num:
            print("Perfect square")
            return
        print("Not Perfect square")

perfect_number(num)