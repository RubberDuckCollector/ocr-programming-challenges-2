from random import randint

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else 0

def main():
    
    operations = ["+", "-", "*", "/"]
    answers_correct = 0

    print("All answers for division are rounded to 1 dp.")

    name = input("Enter your name: ") # will be used after the for loop below

    class_ = int(input("What class are you in (1, 2, 3)? ")) # will be used after the for loop below

    for i in range (1, 11):
        num1 = randint(0, 200)
        num2 = randint(0, 200)

        rand_operation = randint(0, 3)

        match rand_operation:
            case 0:
                computer_answer = add(num1, num2)
                print(f"Question {i}:")
                user_answer = float(input(f"What is {num1} {operations[rand_operation]} {num2}? "))
                if user_answer == computer_answer:
                    print("Correct")
                    answers_correct += 1
                else:
                    print(f"Incorrect, answer is {computer_answer}")
            case 1:
                computer_answer = subtract(num1, num2)
                print(f"Question {i}:")
                user_answer = float(input(f"What is {num1} {operations[rand_operation]} {num2}? "))
                if user_answer == computer_answer:
                    print("Correct")
                    answers_correct += 1
                else:
                    print(f"Incorrect, answer is {computer_answer}")
            case 2:
                computer_answer = multiply(num1, num2)
                print(f"Question {i}:")
                user_answer = float(input(f"What is {num1} {operations[rand_operation]} {num2}? "))
                if user_answer == computer_answer:
                    print("Correct")
                    answers_correct += 1
                else:
                    print(f"Incorrect, answer is {computer_answer}")
            case 3:
                computer_answer = round(divide(num1, num2), 1)
                print(f"Question {i}:")
                user_answer = float(input(f"What is {num1} {operations[rand_operation]} {num2}? "))
                if user_answer == computer_answer:
                    print("Correct")
                    answers_correct += 1
                else:
                    print(f"Incorrect, answer is {computer_answer}")

            case other:
                print("error")

    print(f"Answers correct: {answers_correct} out of 10")

    with open(f"8-arithmetic/8-arithmetic-class-{class_}.txt", "a") as f:
        f.write(f"{name}: {answers_correct}")
        


if __name__ == '__main__':
    main()