from random import *

numbers = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Spades','Hearts','Diamons','Clubs']

player_hand = []
player_wallet = 100
player_score = 0
bet = 0

dealers_hand = []
dealer_score = 0

blackjack = False


def deck_shuffle():
    new_deck = []
    for i in range(len(numbers)):
        for j in range(0,4):
            new_deck.append(f'{numbers[i]} :{suits[j]}')
    shuffle(new_deck)
    return new_deck

def first_deal(deck):
    for i in range(2):
        deck = check_deck(deck)
        player_hand.append(deck.pop(0))
        deck = check_deck(deck)
        dealers_hand.append(deck.pop(0))

def cards_to_score(hand) ->  int:
    score =  0
    aces = 0
    for card in hand:
        if card[0].isdigit():
            if card[1].isdigit():
                score += 10
            else:
                score += int(card[0])
        elif card[0] == "A":
            aces += 1
        else:
            score += 10

    for i in range(aces):
        if score + 11  > 21:
            score += 1
        else:
            score += 11
    return score

def hit(deck):
    player_hand.append(deck.pop(0))

def stand(deck, dealer_score):
    while dealer_score < 16:
        deck = check_deck(deck)
        dealers_hand.append(deck.pop(0))
        dealer_score = cards_to_score(dealers_hand)

def check_deck(deck):

    if len(deck) == 0:
        deck = deck_shuffle()
    return deck

def busted(hand):
    return cards_to_score(hand) >21

def ok_bet(bet: str) -> int:
    while True:
        if not bet.isdigit():
            print("Please input a numerical value.")
        elif int(bet) > player_wallet:
            print("Your bet cannot exceed your balance.")
        else:
            return int(bet)
        bet = input(f"How much is your bet? You have {player_wallet}$: ")

def display_player_hand(player_score):
    print("__This is your hand__")
    print(f"{player_hand} score: {player_score}")

def display_dealer_hand(dealer_score):
    print("__This is the dealer's hand__")
    print(f"{dealers_hand} score: {dealer_score}")

def ok_input(inp):
    while inp != "HIT" and inp != "STAND":
        print("Please enter a valid input")
        inp = input("What is your play?(HIT/STAND)")
    return inp

def reset_hands():
    player_hand.clear()
    dealers_hand.clear()