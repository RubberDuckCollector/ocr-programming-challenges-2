def is_prime(n):

    if n < 2:
        return False
    else:
        # it's (2, n) because we want to test from 2 to n-1
        # this will mean that anything n is divisble by won't be 1 or itself
        for i in range(2, n):
            # if n is divisible by i then it cannot be prime
            # because prime numbers can only be divisible by 1 and themselves
            # the for loop does not touch on 1 or n
            if n % i == 0:
                return False

        return True

def product_of_list(l):
    total = 1

    for i in range(len(l)):
        total *= l[i]

    return total

def prime_factors(n):

    prime_factors_list = []
    i = 2

    while i <= n:
        if n % i == 0:
            prime_factors_list.append(i)
            n //= i
        else:
            i += 1
    return prime_factors_list

print(prime_factors(20))
print(prime_factors(40))
print(prime_factors(100))
print(prime_factors(29))
print(prime_factors(4))
print(prime_factors(6))
print(prime_factors(12))




# TODO: NOT ENOUGH NUMBERS ARE BEING APPENDED INTO prime_factors_list
# TODO: BUT THEY ARE THE CORRECT ONES (prime factors of 20 are 5, 2, 2 OR 5 * 2 squared)
# TODO: IN prime_factors_list YOU NEED TO TAKE THE PRODUCT OF THE WHOLE LIST ON EACH ITERATION AND COMPARE IT TO N
