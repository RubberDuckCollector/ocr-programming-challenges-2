def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(0, 11): # part 1
    print(fib(i))


num_places = int(input("How many places do you want the fibonacci sequence to? ")) # part 2
fib_list = []
for i in range(0, num_places-1):
    fib_list.append(fib(i))


for i in reversed(range(len(fib_list))): # part 3
    print(fib_list[i])
print(f"sum of the numbers: {sum(fib_list)}")
