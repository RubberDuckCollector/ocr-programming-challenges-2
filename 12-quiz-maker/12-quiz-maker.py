from random import randint

questions = []
with open("12-quiz-maker/answers.txt", "r") as f:
    for line in f:
        line = line.strip() # it is indented here because it should happen to every line
        if line: # meaning that if the line is not empty, the following code will execute
            questions.append([line])

# right now each sublist has one element containing the country AND capital in one string.
print(questions)

# this list comprehension splits that string on each ", " for every element in every sublist in the list
questions = [questions[i][0].split(", ") for i in range(len(questions))] # i did this all by myself and i'm very proud
# before the list comprehension, every sublist contains a string. the string has the country, its capital, and a comma
# the list comp splits the string on the comma so now there are 2 strings
# questions[i] is a sublist
# questions[i][0] is the country
# questions[i][1] is the capital
print(questions)


grades_dict = {
    0: "U",
    1: "F",
    2: "E",
    3: "D",
    4: "C",
    5: "C",
    6: "B",
    7: "A",
    8: "A*"
}

questions_correct = 0
question_num = 1
while len(questions) != 0:
    rand_question = randint(0, len(questions)-1)

    print(f"Question {question_num}:")
    prompt = input(f"What is the capital of {questions[rand_question][0]}? ").lower().capitalize()
    if prompt == questions[rand_question][1]:
        print("Correct!")
        questions_correct += 1
    else:
        print(f"Incorrect! Answer is {questions[rand_question][1]}")
    questions.remove(questions[rand_question])

    question_num += 1


if questions_correct in grades_dict:
    print(f"You got {questions_correct} questions correct. Your grade is {grades_dict[questions_correct]}")

# fhi im lizzie