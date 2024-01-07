import random
from random import randint

def make_password():

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "`\"\'|\\[]-=_+~!@£$%^&*(),./<>?#€;:|{}"
    numbers = "1234567890"

    password = ""
    for i in range(0, 12):

        rand_choice = randint(1, 4)
        match rand_choice:
            case 1:
                password += random.choice(lowercase)
            case 2:
                password += random.choice(uppercase)
            case 3:
                password += random.choice(symbols)
            case other:
                password += random.choice(numbers)

    print(password)

    with open("62-R@nd0m-P@ssw0rd--generator.txt", "a") as f:
        f.write(f"{password}\n")

make_password()
