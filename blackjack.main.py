import random

from art import logo

BLACKJACK = 21
CARDS = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

def deal_card():
    """returns the random card from the deck"""
    return random.choice(list(CARDS.keys()))

def calculate_score(cards):
    """calculate the score of all cards"""
    values = [CARDS[card] for card in cards]
    if sum(values) == BLACKJACK and len(values) == 2:
        return BLACKJACK

    while 11 in values and sum(values) > BLACKJACK:
        values[values.index(11)] = 1

    return sum(values)

def compare(u_score, c_score):
    """c_score = calculate_score & u_score = user_score"""
    """comparing players score to find out winner"""
    if u_score == c_score:
        return "Draw 😐"
    elif c_score == BLACKJACK:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == BLACKJACK:
        return "Win with a Blackjack 😎"
    elif u_score > BLACKJACK:
        return "ohh..no. You went over. You lose 😭"
    elif c_score > BLACKJACK:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def get_valid_input():
    while True:
        user_choice = input("Type 'y' to get another card, type 'n' to pass:  \n").strip().lower()
        if user_choice == "yes" or user_choice == "y" or user_choice == "n":
            return user_choice
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")


def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    print(logo)

    """dealing cards"""
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
    for _ in range(2):
        new_card = deal_card()
        computer_cards.append(new_card)

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} | Current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == BLACKJACK or computer_score == BLACKJACK or user_score > BLACKJACK:
            game_over = True
        else:
            if get_valid_input() == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    """computer draws the cards"""
    while computer_score != BLACKJACK and computer_score < 17:
        new_card = deal_card()
        computer_cards.append(new_card)
        computer_score = calculate_score(computer_cards)


    winner = compare(user_score, computer_score)
    print("\n--- Final Results ---")
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(winner)

while True:
    print("\n--- BLACKJACK ---")
    Choice = input("type 'y' if you want to play the game of blackjack, or 'n' for closing the game. ").strip().lower()
    if Choice == "y":
        print("\n" * 100)
        play_game()
    elif Choice == "n":
        print("Thanks for playing! goodbye👋")
        break
    else:
        print("❌ Invalid input. Please type 'y' or 'n'.")


