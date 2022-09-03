import random
import os

################### Our BlackJack Game Rules ############################


# The Deck is Unlimitted in Size
# There are no Jockers
# The Jack/Queen/King all count as 10
# The Ace count as 11/1
# use the following list as the deck of cards 

# create a deal_card() function that use the list below to ** return * random cards 
# 11 is Ace

def deal_card(cards):
    """"
    Return Random card from cards 
    """
    return random.choice(cards)
def calculate_score(cards):
    # Inside calculate_score() function  check for black-jack( a hand with only two cards a + 10) and return 0 instead of the actual score.
    # 0 represent blackjack in our game

    """
    Take a list of Cards and calculate the total sum of cards and return sum
    
    """

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:

        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, Oppenent has BlackJack"

    elif user_score == 0:
        return "Win With BlackJack"

    elif user_score > 21:
        return "You Went Over You Lose"

    elif computer_score > 21:
        return "Computer Went Over You Win"

    elif user_score > computer_score:
        return "You Win"

    else:
        return "You Lost"
def play_game():
       
    
    cards = [
        11,2,3,4,5,6,7,8,9,10,10,10,10
    ]
    
    # Deal the User and Computer Each 2 cards using deal_card() function
    user_cards = []
    computer_cards = []
    
    is_game_over = False
    
    for i in range(2):
        card = deal_card(cards = cards)
    
        user_cards.append(card)
    
    for _ in range(2):
        card = deal_card(cards = cards)
        computer_cards.append(card)
    
    
    
    
    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f" Your Cards: {user_cards}, Your Current Score is {user_score}")
        print(f" Computer's First card is {computer_cards[0]}: ")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        
        else:
            user_should_deal = input(" type 'y' to get another card  or type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card(cards = cards))
        
            else:
                is_game_over = True
    
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards = cards))
        computer_score = calculate_score(computer_cards)
    
    print(f"Your Final hand is: {user_cards} and Your Final Score is: {user_score}")
    print(f"Computer Final hand is: {computer_cards} and Computer Final Score is: {computer_score}")
    
    print(compare(user_score = user_score, computer_score = computer_score))
    

    
    
    # The Cards in the list have equal probalbity of bring drawn
# Cards are not removed fro the deck as they are being drawn
while input("Do You want to play Blackjack game? Type 'y' or 'n' ") == "y":
    os.system('clear')
    play_game()