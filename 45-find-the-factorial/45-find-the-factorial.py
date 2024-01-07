def factorial_iterative(n):

    if n == 0:
      return 1
  
    counter = 1

    for i in range(1, n + 1):
        counter = counter * i

    return counter

print(factorial_iterative(5))

def factorial_recursive(n):
  
    if n == 0:
      return 1
    
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
print(factorial_recursive(5))