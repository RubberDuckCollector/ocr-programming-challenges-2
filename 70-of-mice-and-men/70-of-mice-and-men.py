from random import randint


def main():
    
    mouse = 0 
    man = 0

    rand_num = [randint(0, 9) for _ in range(4)]
    print(f"rand_num: {rand_num}")


    user_input_num = 0
    while True:
        try:
            user_input_num = input("Enter a 4 digit number: ")

            user_input_num = list(map(int, user_input_num))
            if len(user_input_num) == 4:
                break
            else:
                print("Enter a number between 0000 and 9999 inclusive.")

            for i in range(len(rand_num)):
                if rand_num[i] == user_input_num[i]:
                    mouse += 1
                elif 
        except ValueError:
            print("Try again.")
    print(user_input_num)


if __name__ == "__main__":
    main()
