import random
from art import logo

user_cards = []
computer_cards = []
computer_first_card = []
game_over = False
black_jack = 21
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def final_score():
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if computer_score > 21:
        print("Computer went over ! You win 🥳")
    elif user_score > 21:
        print("You went over ! You lose 😭")
    elif computer_score > user_score:
        print("You lose !")
    elif user_score > computer_score:
        print("You win !")
    else:
        print("it's a draw! ")


def another_draw():
    while True:
        my_score = calculate_score(user_cards)
        if my_score > 21:
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if another_card == "y":
            user_cards.append(random.choice(deck))
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_first_card}")
        else:
            break
    computer_turn()


def computer_turn():
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(deck))
    final_score()


def card_draw():
    global user_cards, computer_cards, computer_first_card
    user_cards = random.sample(deck, 2)
    computer_cards = random.sample(deck, 2)
    computer_first_card = computer_cards[0]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(logo)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_first_card}")

    if computer_score == black_jack:
        print("Computer wins with a Blackjack! 😭")
    elif user_score == black_jack:
        print("You win with a Blackjack! 🥳")
    else:
        another_draw()


while not game_over:
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game == "y":
        card_draw()
    else:
        game_over = True
