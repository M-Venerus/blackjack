import random

def deal_card():
    """Return a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 ,10]
    return random.choice(cards)

def calculate_score(cards_list):
    """Calculate score by sum of card values in a list. Automatically turn Ace to '1' if necessary. 
    Return a value of '0' when sum equals 21 as a Blackjack win."""
    total = sum(cards_list)
    if total == 21:
        return 0
    if (11 in cards_list) and (total > 21):
        cards_list.remove(11) 
        cards_list.append(1)
    return sum(cards_list)

def compare(computer_score, user_score):
    """Display and compare the sum values of two lists according to Blackjack rules and produce a winner."""
    print(f"Computer's final hand: {computer_cards} = {sum(computer_cards)}")
    print(f"User's final hand: {user_cards} = {sum(user_cards)}")
    if computer_score == user_score:
        print("Its a draw.")
    elif computer_score == 0:
        print("You lose")
    elif user_score == 0:
        print("Blackjack! You win!")
    elif user_score > 21:
        print("You lose.")
    elif computer_score > 21:
        print("You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose.")

playing_game = True

while playing_game:
    print("Welcome to Blackjack!")

    user_cards = []
    computer_cards = []

    for repeat in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    game_stop = False

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if user_score == 0 :
        game_stop = True
    print(f"Computer: [{computer_cards[0]}, ?] = ?")
    print(f"User: {user_cards} = {sum(user_cards)}")

    while game_stop != True:

        user_continue = input("Do you want to draw another card? 'y' or 'n': ")
        if user_continue == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if (user_score== 0 ) or (user_score > 21 ):
                game_stop = True
            else:
                print(f"Computer: [{computer_cards[0]}, ?] = ?")
                print(f"User: {user_cards} = {sum(user_cards)}")
        else: game_stop = True

    while 0 < computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(computer_score, user_score)

    play_again = input("Do you want to play again? 'y' or 'n': ")
    if play_again == "n":
        playing_game = False

print("Thanks for playing! Goodbye.")
