import random

def play_again():
  answer = input("Do you want to play again? (yes/no): ").lower()
  return answer == "yes"

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  if user_choice == "rock" and computer_choice == "scissors":
    return "You win! Rock crushes scissors."
  elif user_choice == "paper" and computer_choice == "rock":
    return "You win! Paper covers rock."
  elif user_choice == "scissors" and computer_choice == "paper":
    return "You win! Scissors cut paper."
  else:
    return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

def main():
  user_score = 0
  computer_score = 0

  print("Welcome to Rock-Paper-Scissors!")

  while True:
    print("\nChoose one (rock, paper, or scissors) : ")
    user_choice = input("> ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    while user_choice not in valid_choices:
      print(f"Invalid choice. Please choose rock, paper, or scissors.")
      user_choice = input("> ").lower()
    computer_choice = random.choice(valid_choices)

    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    if result.startswith("You win"):
      user_score += 1
    elif result.find("lose") != -1:
      computer_score += 1
    print(f"\nYour score: {user_score}")
    print(f"Computer score: {computer_score}")

    if not play_again():
      print("\nThanks for playing!")
      break

if __name__ == "__main__":
  main()
