def fizz_buzz_simple():


    for i in range(1, 101):
        output = ""
        if i % 3 == 0 and i % 5 == 0:
            output += "FizzBuzz"
        elif i % 3 == 0:
            output += "Fizz"
        elif i % 5 == 0:
            output += "Buzz"
        else:
            output = str(i)
        
        print(output)

# fizz_buzz_simple()

def fizz_buzz_complicated():

    for i in range(1, 101):
        print("Fizz Buzz") if i % 3 == 0 and i % 5 == 0 else None
        print("Fizz") if i % 3 == 0 else None
        print("Buzz") if i % 5 == 0 else None
        print(i) if i % 3 != 0 and i % 5 != 0 else None

fizz_buzz_complicated()

def check_prime(n):

    if n == 1:
        return False
    elif n > 1:
        for i in range(2, n): # starts at 2 because all ints are divisible by 1
            if n % i == 0:
                """
                # this is false because if n is divisible y i,
                then it must have more than 2 factors (which would be more than 1 and itself,
                meaning that n is not prime)
                """
                return False
        return True # otherwise n is prime if the if statement has not been triggered

def fizz_buzz_extension(n, f, b): # this takes n as the parameter

    """
    the for loop goes up until n + 1. e.g: if n = 100,
    it means that the foor loop is basically `for i in range(1, 101):` because
    n = 100 so n + 1 is 101 so 101 is inserted into the for loop
    """
    for i in range(1, n+1):
        output = ""

        if check_prime(i):
            output += "OOPS!"
        elif i % f == 0 and i % b == 0:
            output += "FizzBuzz"
        elif i % f == 0:
            output += "Fizz"
        elif i % b == 0:
            output += "Buzz"
        else:
            output = str(i)
        
        print(f"{i}: {output}")

# order of parameters: (number to go to, fizz value, buzz value)
# fizz_buzz_extension(100, 3, 5)
# fizz_buzz_extension(100, 2, 3)
