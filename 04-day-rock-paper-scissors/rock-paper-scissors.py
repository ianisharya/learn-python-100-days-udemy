import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices_list = ['rock', 'paper', 'scissors']

art = {
    'rock': rock,
    'paper': paper,
    'scissors': scissors
}

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

print('Welcome to Rock, Paper, Scissors!\n')

user_score = 0
computer_score = 0
separator = '\n------\n'
num_rounds = 0

while True:

    num_rounds += 1
    print(f"\n--- Round {num_rounds} ---")

    # Get user input
    while True:
        user_choice = input('What do you choose? "rock", "paper", "scissors":\n').lower()
        if user_choice not in choices_list:
            print('Wrong choice! Try again.', end = separator)
        else:
            break

    # Computer choice
    computer_choice = random.choice(choices_list)

    # Show choices with art
    print(f'\nYou chose: {user_choice}')
    print(art[user_choice], end = separator)

    print(f'Computer chose: {computer_choice}')
    print(art[computer_choice], end = separator)

    # Decide winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif wins[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Show score
    print(f"\nTotal Rounds: {num_rounds} | Score ->  You: {user_score} | Computer: {computer_score}", end = separator)

    # Play again?
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("\nThanks for playing!")
        break
