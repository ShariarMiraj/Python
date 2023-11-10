# Creat a program capable of displaying qustions to the user loike KBC 
# Use List data type to store the qustions and their correct answer .
# Display the final amount the person is taking home after playing the game.


import random

# Function to display questions and get user input
def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = int(input("Your answer (enter the corresponding option number): "))
    return user_answer

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to play the quiz game
def play_game(questions):
    total_questions = len(questions)
    money = 0

    for i, (question, options, correct_answer, prize) in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{total_questions}:")
        user_answer = display_question(question, options)

        if check_answer(user_answer, correct_answer):
            print("Correct answer! You win", prize)
            money += prize
        else:
            print("Incorrect answer. Game over!")
            break

    print(f"\nCongratulations! You are taking home a total of {money}.")

# List of questions with format: (question, options, correct_answer, prize)
questions = [
    ("What is the capital of France?", ["A. Paris", "B. Berlin", "C. Rome", "D. Madrid"], 1, 1000),
    ("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], 2, 5000),
    ("What is the largest mammal in the world?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"], 2, 10000),
    ("Who wrote 'Romeo and Juliet'?", ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], 2, 50000),
    ("What is the currency of Japan?", ["A. Won", "B. Yen", "C. Peso", "D. Euro"], 2, 100000),
    # Add more questions as needed
]

# Shuffle the questions for a random order each time
random.shuffle(questions)

# Start the game
play_game(questions)





# import random

# # Questions list with their respective correct answers
# questions = [
#     ['Question 1', 'Answer 1'],
#     ['Question 2', 'Answer 2'],
#     ['Question 3', 'Answer 3'],
#     ['Question 4', 'Answer 4'],
#     ['Question 5', 'Answer 5'],
# ]

# # User's winnings initially set to zero
# winnings = 0

# # Randomly select questions and provide options for user to choose
# for i in range(3):
#     random_question = random.choice(questions)
#     print(f"\nQ. {random_question[0]}")
#     print(f"1. {random_question[1]}")
#     print(f"2. Wrong Answer 2")
#     print(f"3. Wrong Answer 3")

#     # User input
#     user_answer = int(input("Enter your choice: "))

#     # Check if user's answer is correct and update winnings accordingly
#     if user_answer == 1:
#         winnings += 1000
#         print("Correct Answer! You win 1000!")
#     else:
#         print("Wrong Answer! Better luck next time!")

# print(f"\nYour final winnings are: ₹{winnings}")
