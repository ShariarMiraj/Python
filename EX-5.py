import random

def cheack(comp,user):
  if comp==user:
    return 0

  if(comp == 0 and user == 1):
    return -1

  if(comp == 1 and user == 2):
    return -1

  if(comp == 2 and user == 0):
    return -1

  return 1


comp = random.randint(0,2)
user = int(input("0 for snake, 1 for water and 2 for gun:\n"))

score = cheack(comp,user)
print("You: ", user)
print("Computer: ", comp)      


if(score == 0):
  print("It is a DraW..Match.!")
elif(score == -1):
  print("You Lose..!")
else:
  print("You won this Match..!")














  # this is from chAT GPT

  import random

  def get_user_choice():
      user_choice = input("Enter your choice (snake, water, or gun): ").lower()
      while user_choice not in ['snake', 'water', 'gun']:
          print("Invalid choice. Please enter snake, water, or gun.")
          user_choice = input("Enter your choice (snake, water, or gun): ").lower()
      return user_choice

  def get_computer_choice():
      return random.choice(['snake', 'water', 'gun'])

  def determine_winner(user_choice, computer_choice):
      if user_choice == computer_choice:
          return "It's a tie!"
      elif (user_choice == 'snake' and computer_choice == 'water') or \
           (user_choice == 'water' and computer_choice == 'gun') or \
           (user_choice == 'gun' and computer_choice == 'snake'):
          return "You win!"
      else:
          return "Computer wins!"

  def play_game():
      print("Welcome to Snake Water Gun Game!")

      while True:
          user_choice = get_user_choice()
          computer_choice = get_computer_choice()

          print(f"You chose {user_choice}")
          print(f"Computer chose {computer_choice}")

          result = determine_winner(user_choice, computer_choice)
          print(result)

          play_again = input("Do you want to play again? (yes/no): ").lower()
          if play_again != 'yes':
              print("Thanks for playing. Goodbye!")
              break

  if __name__ == "__main__":
      play_game()

  
    