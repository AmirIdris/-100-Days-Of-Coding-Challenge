import random

number_to_be_guessed = []

for i in range(100):
    number_to_be_guessed.append(i)


print("Welcome to The Number Guessing Game!")
print("I'm thinking of Number between 1 and 100")
direction = input("Choose Difficulty. Type 'easy' or 'hard': ")


if direction == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number")





selected_number = random.choice(number_to_be_guessed)

is_game_over = False
while not is_game_over and attempts > 0:
    guess = int(input("Make a guess: "))



    if guess > selected_number:
        print("Too Haigh.")
        print("Guess again.")
        attempts = attempts - 1
        print(f"You Have {attempts} attempts remaining to guess the number.")

    
    
    elif guess < selected_number:
        print("Too Low.")
        print("Guess again.")
        attempts = attempts -1
        print(f"You Have {attempts} attempts remaining to guess the number.")
    
    else:
        print("Correct. \n")
        print(f"You got it the answer were {guess}.")
        is_game_over = True

  
if attempts == 0:
    print("You Have run Out of guess, you lose")
    is_game_over = True 
    
    
