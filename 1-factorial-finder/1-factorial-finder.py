def factorial_iterative(n):

    """
    - parameter n mst be postive

    the for loop starts at 1, and goes until n + 1
    (i.e if parameter n = 5, the for loop will basicaly be `for i in range(1, 6)` and will stop before reaching 6)

    counter starts at 1, and is multiplied by i which also starts at 1
    1 * 1 = 1

    then i increments to make the calculation 1 * 2
    counter is now 2

    then i increments again, so the calculation is 2 * 3 (i is 3) (2 is counter, 1 * 2)

    counter = counter * i and counter is 2 so 2 * 3 is 6 (i is equal to 3)

    6 * 4 = 24 (counter * i)

    24 * 5 = 120 (counter * i)
    """
    
    counter = 1

    for i in range(1, n + 1):
        counter = counter * i

    return counter

print(factorial_iterative(10))

def factorial_recursive(n):

    """
    - parameter n must be positive

    `if n == 1` is the stopping condition. you must have this and 2 other requirements
    to consider a subroutine to be recursive

    if n is 1, then return 1 (1 * 1-1 is the same as 1 * 0 which is math error) so 

    for ALL other numbers, return n times the factorial of n - 1

    if the parameter n is 5, it multiplies the result of the recursive factorial function call,
    which takes n-1 as its parameter (meaning 4 is passed).

    this happens again where 4 is multiplied by the output of the parameter 4-1

    then 3 is multiplied by the output of 3-1

    same for 2-1

    when the stopping condition is reached, the function calls unwind starting at the bottom
    these function calls feed into each other as is the nature of recursion

    2 * factorial(1) = 2 * 1 = 2
    - the answer to this (2) feeds into the next level up:

    3 * factorial(2) =  3 * 2 = 6 (this 2 is from the answer of 2 factorial(1))

    4 * factorial(3) = 4 * 6 = 24 (the 6 is from the answer to 3 * factorial(2))

    5 * factorial(4) = 5 * 24 = 120

    120 is the final output that is returned for this example where parameter n is 5.
    """

    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
print(factorial_recursive(5))
