import random
# step 1
word_list = ["ardvark","baboon", "camel"]

# TODO-1 randomly pick word from the list and 
# assign to chosen_word

chosen_word = random.choice(word_list)
print(chosen_word)
# generate blank space of equal size to chosen words 

letter_to_guess = []
for i in range(len(chosen_word)):
    letter_to_guess.append("_")

print(letter_to_guess)

# TODO-2 ask the user to guess letter and store it to variable called guess

guess = input("guess the letter ").lower()


# TODO-3 check if the letter the user guessed is one of the letter in the words   
lives = 6
win = 0
while "_"   in letter_to_guess and lives > 0:
    for index,char in enumerate(chosen_word):
        if (guess == char):
            letter_to_guess[index] = char
            print(letter_to_guess)

    if guess  not in letter_to_guess:
        lives = lives - 1
        print(f"You only left with {lives}")  

    if "_" in letter_to_guess:
        guess = input("guess the letter ").lower()

    else:
        win = 1
        print("congratulation you won the game")

if win == 0:
    print("You have lost the game")



