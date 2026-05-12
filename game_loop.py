
from deck import Deck
from player import Player
from turn import Turn
from card import Card
from sys import exit
from random import randint
from dialogue import *

# game actions

def dealing(deck, player, other):
    counter = 0
    while counter <= 6:
        
        deck.draw(player)
        player.display_hand()

        counter += 1

    deck.draw(dealer)


def play(deck, player, dealer, turn):
    print("Welcome to Lucky!\n")
    print("Play all your cards before the deck reaches 0 to win\n")

    while True:
        # special conditions
        if turn.get_turn() == 0:
            deck.shuffle()
            deck.shuffle()
            deck.shuffle()

            dealing(deck, player, dealer)
            
            turn.update_turn()
        elif is_victory(player):
            print("GAME OVER!\n")
            report(deck, player, dealer, turn)
            exit()
        elif is_defeat(deck, player):
            print("GAME OVER\n")
            report(deck, player, dealer, turn)
            exit()
        
        dealer_card_obj = dealer.get_hand()[-1]
        
        print()
        deck.display_deck_count()
        turn.display_turn()
        display_current_card(dealer)
        print()
        player.display_hand()


        action = input("Select a card: \n> type color number/draw/quit\n").lower()
        
        if action == "draw":
            draw(deck, player, turn_count)
            turn.update_turn()
            continue
        elif action == "quit":
            exit()
        elif player.is_card_in_hand(action):
                card_obj = player.played_card(action)
                
                if card_obj.is_comparable(dealer_card_obj):
                    player.remove_card(action)
                    
                    dealer.update_hand(card_obj)
                    
                    turn.update_turn()
                    continue
                else:
                    print("incorrect card type")
                    continue
        else:
         print("invalid action")
         continue


def draw(deck, player, turn):
    deck.draw(player)
    # punishing the player
    if turn.get_turn() >= 5 and turn.get_turn() < 10:
        deck.remove_cards(1)
    elif turn.get_turn() >= 10:
        random_amount = randint(1, 2)
        deck.remove_cards(random_amount)

    if player.is_max_hand():
        print("\n" + shredded_from_hand[randint(0, len(shredded_from_hand) - 1)])
        missing_card = player.remove_random_card()
        print(f"{missing_card.get_card()} has been removed from hand")

# game status

def display_current_card(dealer):
    current_card = dealer.get_hand()[-1].get_card()
    print(f"Dealer: {current_card}")


def is_victory(player):
    if player.get_hand_count() == 0:
        return True    
    return False

def is_defeat(deck, player):
    if deck.get_deck_count() == 0 and player.get_hand_count() > 0:
        return True
    return False

def report(deck, player, dealer, turn):
    if is_victory(player):
        outcome = "VICTORY!"
    else:
        outcome = "DEFEAT..."
    print("CREDITS")
    print(outcome)
    print(f" You played {dealer.get_hand_count() - 1} cards")
    print(f"Turns taken {turn.get_turn()}")
    print(f"Cards in deck remaining {deck.get_deck_count()}")
    print()
    print("Created by: Katana")


# initialize objects

deck = Deck()
deck.make_deck()

player = Player()

dealer = Player()

turn_count = Turn()

play_game = play(deck, player, dealer, turn_count)

