def fib(n):

    a = 0
    b = 1

    c = 0

    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c # is the nth term of the sequence

i = 1
while True:
    
    # int to str conversions currently use an n squared algorithm maybe there's a more efficient way
    a = str(fib(i))
    print(a)

    if len(a) >= 1000:
        print(f"\n{a}")
        print(f"the {i} term of the fibonacci sequence is the first one with 1000 digits")
        break

    i += 1
