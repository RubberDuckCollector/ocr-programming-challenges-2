import itertools

def find_combinations(num):

    num = str(num)

    return list(itertools.permutations(num))

print(find_combinations(1234))

# 24 numbers can arise from a given 4 digit number
# which is 4!
# if the number has repeated digits it is less than 24
