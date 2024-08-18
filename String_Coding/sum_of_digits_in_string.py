str = "Si6d123u45"

def check(str):
    sum = 0
    for i in str:
        if i.isdigit():
            inte = int(i)
            sum = sum+inte
    print(sum)

check(str)