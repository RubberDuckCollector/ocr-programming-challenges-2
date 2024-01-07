import copy
import random
from random import randint

def set_example():
    alphabet = "abcdefghijklmnopqrstuvxyz"

    nums = [21, 39, 15, 70, 23, 38, 21, 2, 96, 39]
    nums2 = copy.deepcopy(nums)

    print(nums)
    nums.sort()
    print(f"ordered small to large: {nums}", "\n")

    even = [i for i in nums if i % 2 == 0] # for every element of l, append to even if the number at i is even
    odd = [i for i in nums if i % 2 != 0] # same but odd

    print(even)
    print(odd)

    print(f"even numbers last: {odd + even}") # even numbers are after odd numbers now
    print(f"original: {nums2}") # original

    letters = ["d", "g", "a", "x"]

    letters.sort()
    letters = letters[::-1]

    print(letters)

    print(f"reverse letters, odd, even: {letters + odd + even}")

def random_example(): # this one answers the question

    alphabet = "abcdefghijklmnopqrstuvxyz"

    nums = []

    for i in range(10):
        nums.append(randint(0, 100))

    nums2 = copy.deepcopy(nums)

    print(nums)
    nums.sort()
    print(f"ordered small to large: {nums}", "\n")

    even = [i for i in nums if i % 2 == 0] # for every element of l, append to even if the number at i is even
    odd = [i for i in nums if i % 2 != 0] # same but odd

    print(even)
    print(odd)

    print(f"even numbers last: {odd + even}") # even numbers are after odd numbers now
    print(f"original: {nums2}") # original

    letters = []

    for i in range(10):
        letters.append(random.choice(alphabet))

    letters.sort()
    letters = letters[::-1]

    print(letters)

    print(f"reverse letters, odd, even: {letters + odd + even}")

random_example()
