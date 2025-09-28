def check(start,end):
    for i in range(start,end):
        if i>=2:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    print(i,"is not a prime number")
                    break
            else:
                print(i," is Prime number")
check(1,100)
