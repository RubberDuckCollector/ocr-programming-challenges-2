def happy_numbers(num):
    num = str(num) # "234"

    num_digits = list(num) # turns "234" into a list containing "2" "3" and "4"

    num_digits = list(map(int, num_digits)) # turns all of the strs in the list into ints

    mapped = list(map(lambda num: num ** 2, num_digits)) # because the list is of ints, we can use an anonymous func to square all ints in the list

    num = sum(mapped)

    return num

def find_happy_numbers(b):
    happy_list = []
    count = 0

    while b not in happy_list and count < 50:
        happy_list.append(b)
        b = happy_numbers(b)
        count += 1
    return b == 1

happy = []

for i in range(1, 101):
    if find_happy_numbers(i):
        print(f"yes {i}")
        happy.append(i)
    else:
        print(f"no")

print(happy)
