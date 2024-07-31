num1 = 35
num2 = 59
num3 = 45
def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is greater than",num2,"and",num3)
    elif num2>num1 and num2>num3:
        print(num2,"is greater than",num1,"and",num3)
    else:
        print(num3, "is greater than", num1, "and",num2)

greatest(num1,num2,num3)