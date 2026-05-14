
from deck import Deck
from player import Player
from turn import Turn
from card import Card
from sys import exit
from random import randint
from dialogue import *
from os import system
from time import sleep


# game actions

def dealing(deck, player, other):
    counter = 0
    while counter <= 6:
        
        deck.draw(player)
        player.display_hand()

        counter += 1
        sleep(1)

    deck.draw(dealer)


def play(deck, player, dealer, turn):
    global select_mode
    print("Welcome to Lucky!\n")
    print("Play all your cards before the deck reaches 0 to win\n")
    sleep(2)

    while True:
        update_screen()
        try:
            select_mode = input("Please enter a mode:\n> easy/medium/hard").lower()
        except KeyboardInterrupt:
            exit()
        if select_mode == mode(select_mode):
            break
        elif select_mode == "quit":
            exit()
        else:
            print("invalid mode")

    while True:
        # special conditions
        if turn.get_turn() == 0:
            deck.shuffle()
            deck.shuffle()
            deck.shuffle()
            update_screen()

            dealing(deck, player, dealer)
            
            turn.update_turn()
        elif is_victory(player):
            update_screen()
            print("GAME OVER!\n")
            report(deck, player, dealer, turn)
            exit()
        elif is_defeat(deck, player):
            update_screen()
            print("GAME OVER\n")
            report(deck, player, dealer, turn)
            exit()
        
        dealer_card_obj = dealer.get_hand()[-1]
        
        #print()
        update_screen()

        deck.display_deck_count()
        turn.display_turn()
        display_current_card(dealer)
        print()
       # warn player
        display_warning(turn)

        player.display_hand()


        try:
            action = input("Select a card: \n> type color number/draw/quit").lower()
        except KeyboardInterrupt:
            exit()
        
        if action == "draw":
            if is_easy():
                easy_punishments(deck, turn)
            elif is_medium():
                medium_punishments(deck, turn)
            elif is_hard():
                hard_punishments(deck, turn)

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
         sleep(0.5)
         continue


def draw(deck, player, turn):
    if player.is_max_hand():
        print("\n" + shredded_from_hand[randint(0, len(shredded_from_hand) - 1)])
        missing_card = player.remove_random_card()
        print(f"{missing_card.get_card()} has been removed from hand")
        sleep(1)
    
    deck.draw(player)

# game status

def update_screen():
    sleep(0.5)
    system("clear||cls")


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
    print(f"Difficulty: {mode(select_mode)}")
    print(f" You played {dealer.get_hand_count() - 1} cards")
    print(f"Turns taken {turn.get_turn()}")
    print(f"Cards in deck remaining {deck.get_deck_count()}")
    print()
    print("Created by: Katana")

# modes

def mode(user_mode):
    if user_mode == "easy":
        return "easy"
    elif user_mode == "medium":
        return "medium"
    elif user_mode == "hard":
        return "hard"

def is_easy():
    if mode(select_mode) == "easy":
        return True
    return False

def is_medium():
    if mode(select_mode) == "medium":
        return True
    return False


def is_hard():
    if mode(select_mode) == "hard":
        return True
    return False

# punishments

def easy_punishments(deck, turn):
    if turn.get_turn() >= 5 and turn.get_turn() < 10:
        deck.remove_cards(1)
    elif turn.get_turn() >= 10:
        random_amount = randint(1, 2)
        deck.remove_cards(random_amount)

def medium_punishments(deck, turn):
    if turn.get_turn() >= 1 and turn.get_turn() < 5:
        deck.remove_cards(1)
    elif turn.get_turn() >= 5 and turn.get_turn() < 20:
        random_num = randint(1, 3)
        deck.remove_cards(random_num)
    elif turn.get_turn() >= 20:
        random_num = randint(2, 3)
        deck.remove_cards(random_num)

def hard_punishments(deck, turn):
    if turn.get_turn() >= 1 and turn.get_turn() < 10:
        deck.remove_cards(2)
    elif turn.get_turn() >= 10 and turn.get_turn() < 20:
        random_num = randint(2, 3)
        deck.remove_cards(random_num)
    elif turn.get_turn() >= 20:
        deck.remove_cards(3)

# print warnings

def display_warning(turn):
    if is_easy():
        if turn.get_turn() == 5:
            print("DRAW CAUTION\n")
        elif turn.get_turn() == 10:
            print("DRAW CAUTION\n")
    
    if is_medium():
        if turn.get_turn() == 1:
            print("DRAW CAUTION\n")
        elif turn.get_turn() == 5:
            print("DRAW CAUTION\n")
        elif turn.get_turn() == 20:
            print("DRAW CAUTION\n")
    
    if is_hard():
        if turn.get_turn() == 1:
            print("DRAW CAUTION\n")
        elif turn.get_turn() == 5:
            print("DRAW CAUTION\n")
        elif turn.get_turn() == 20:
            print("DRAW CAUTION\n")

# initialize objects

deck = Deck()
deck.make_deck()

player = Player()

dealer = Player()

turn_count = Turn()

play_game = play(deck, player, dealer, turn_count)

