def check(str):
    lt = list(str)
    i = 0
    while i < len(lt):
        if lt[i] in ['[', ']', '{', '}', '(', ')']:
            lt.pop(i)  # Remove and shift
        else:
            i += 1              # incrementing only when an element is not removed
    s = "".join(lt)
    print(s)

str = "a-(b+c)"
check(str)

