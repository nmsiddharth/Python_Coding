num = int(input("Enter number"))
ones = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]
twos = ["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
hundred = "hundred"
thousand = "thousand"

def check(num):
    if num<0 or num>9999:
        print("Invalid")
    else:
        a = num%10         # last digit
        b = num//10
        c = b%10            # second last digit
        d = num//100
        e = d%10               # third last digit
        f = num//1000           # first digit

    if num>0 and num<20:
        print(ones[num])
    elif num>20 and num<100:
        print(twos[c]+" "+ones[a])
    elif num>100 and num<1000:
        print(ones[e]+" "+hundred+" "+twos[c]+" "+ones[a])
    else:
        print(ones[f]+" "+thousand+" "+ones[e]+" "+hundred+" "+twos[c]+" "+ones[a])


check(num)