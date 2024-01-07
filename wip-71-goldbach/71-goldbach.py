def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    num = int(input("Enter a number "))
    while True:
        if num % 2 == 0 and num > 0:
            print("num is positive and divisible by 2")
            break
        else:
            num = int(input("Enter a number "))

    # create a list of all numbers in between 2 and num
    # filter the list for only the primes

    primes_in_between = []

    nums_in_between = [i for i in range(2, num)]

    for i in range(len(nums_in_between)):
        if is_prime(nums_in_between[i]):
            primes_in_between.append(nums_in_between[i])
    print(primes_in_between)


if __name__ == "__main__":
    main()
