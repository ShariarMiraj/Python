import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/' and num1 % num2 != 0:
        num1, num2 = num2, num1  # Ensure a division with no remainder
    question = f"What is {num1} {operator} {num2}? "
    answer = eval(str(num1) + operator + str(num2))
    return question, answer

def quiz():
    score = 0
    num_questions = 5

    print("Welcome to the Math Quiz!")
    print("Answer the following questions.")

    for _ in range(num_questions):
        question, answer = generate_question()
        user_answer = float(input(question))
        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.\n")

    print(f"Quiz completed. You got {score}/{num_questions} questions correct!")

if __name__ == "__main__":
    quiz()
