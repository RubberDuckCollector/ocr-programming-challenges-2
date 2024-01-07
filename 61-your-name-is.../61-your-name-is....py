def main():

    name = input("enter your name ")

    age = int(input("enter your age "))

    form = input("enter your form ")

    with open("61-your-name-is....txt", "w") as f:
        f.write(f"{name}, {age}, {form}")

    print(f"Your name is {name}, you are {age} years old, and you are in form {form}")




if __name__ == '__main__':
    main()