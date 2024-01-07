# part 1
def part_one():
    username = input("Enter a username: ")
    print(f"Username: {username}")

    while True:
        password = input("Enter a password: ")
        confirm_password = input("Enter a password: ")

        if password != confirm_password:
            print("Passwords do not match")
        else:
            break

    with open("24-hack-proof.txt", "a") as f:
        f.write("Hello world")

# extensions
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "`\"\'|\\[]-=_+~!@£$%^&*(),./<>?#€;:|{}"

def create_password():

    from random import randint

    num_of_chars = randint(8, 16)

    password = ""
    for i in range(num_of_chars):

        rand_choice = randint(1, 3)

        # add random char
        rand_lower = randint(0, len(lowercase)-1)
        rand_upper = randint(0, len(uppercase)-1)
        rand_symbol = randint(0, len(symbols)-1)

        match rand_choice:
            case 1:
                password += lowercase[rand_lower]
            case 2:
                password += uppercase[rand_upper]
            case 3:
                password += symbols[rand_symbol]
    
    return password

def check_password(password): # returns True if the password matches the 5 requirements, otherwise return False

    requirements = 0 # this should be a minimum of 0 and a maxmimun of 4

    if len(password) > 7:
        requirements += 1

    for i in range(len(password)):
        if password[i] in lowercase:
            requirements += 1
            break
    
    for i in range(len(password)):
        if password[i] in uppercase:
            requirements += 1
            break

    for i in range(len(password)):
        if password[i] in symbols:
            requirements += 1
            break

    if requirements == 4:
        return True
    else:
        return requirements


def extensions():
    username = input("Enter a username: ")
    print(f"Username: {username}")

    while True:
        p = create_password()
        print(f"Recommended password: {p}")
        user_password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")

        checker = check_password(user_password)

        if user_password != confirm_password:
            print("Passwords do not match")
        elif checker != True:
            print("Your password did not meet one of these 4 requirements:\nIt needs to be 8 or more characters in length,\nIt needs to have at least one uppercase character,\nIt needs to have at least one lowercase character,\nIt needs to have at least one symbol")
            print(f"Your password met {checker} conditions")
        else:
            print("You've been accepted!")
            break

    with open("24-hack-proof.txt", "a") as f:
        f.write("Hello world\n")



def main():
    extensions()

if __name__ == '__main__':
    main()


