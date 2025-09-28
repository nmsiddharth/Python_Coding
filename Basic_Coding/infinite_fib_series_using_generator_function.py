def fib():
    a,b = 0,1
    while True:
        yield a
        a,b=b,a+b
out = fib()

# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))

for i in range(10):
    print(next(out))    