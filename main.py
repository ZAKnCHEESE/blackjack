from random import *
from functions import *


deck = deck_shuffle()
while player_wallet != 0: 
     # game is being played
    reset_hands()
    player_move = ""
    first_deal(deck)
    player_score = cards_to_score(player_hand)
    dealer_score = cards_to_score(dealers_hand)
    bet = input(f"How much is your bet? you have {player_wallet}$: ")
    bet = ok_bet(bet)
    player_wallet -= bet

    while not busted(player_hand) and player_move != "STAND":
        display_dealer_hand(dealer_score)
        display_player_hand(player_score)

        player_move = input("What is your play? (HIT/STAND)")
        player_move = ok_input(player_move)

        if player_move == "HIT":
            hit(deck)
            player_score = cards_to_score(player_hand)
        else:
            stand(deck, dealer_score)

    if busted(player_hand):
        display_dealer_hand(dealer_score)
        display_player_hand(player_score)
        print("You busted!")
        # Handle losing bet here
    else:
        print("Player stands.")
        while dealer_score < 16:
            stand(deck, dealer_score)
            dealer_score = cards_to_score(dealers_hand)
            
        if busted(dealers_hand):
            display_dealer_hand(dealer_score)
            display_player_hand(player_score)
            print("Dealer busted. You win!")
            player_wallet += bet * 2

        elif dealer_score > player_score:
            display_dealer_hand(dealer_score)
            display_player_hand(player_score)
            print("Dealer wins!")
            print("womp womp")
        elif dealer_score < player_score:
            display_dealer_hand(dealer_score)
            display_player_hand(player_score)
            print("You win!")
            player_wallet += bet * 2
        else:
            display_dealer_hand(dealer_score)
            display_player_hand(player_score)
            print("It's a tie!")
            player_wallet += bet

