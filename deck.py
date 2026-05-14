
import random
from player import Player
from card import Card
from dialogue import *

COLORS = ["blue", "green", "red", "yellow"]
NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Deck:
    def __init__(self):
        self.deck = []

    def get_deck_count(self):
        return len(self.deck)


    def make_deck(self):
        card_pair_obj = []
        for color in COLORS:
            for num in NUMS:
                card_pair_obj.append(Card(color, num))

        # turn instance of class into card class
        for card_obj in card_pair_obj:
            self.deck.append(card_obj)

        self.deck += self.deck
        self.deck


    def shuffle(self):
        length = len(self.deck)
        shuffle_deck = []
        for i in range(len(self.deck)):
            
            select_random_num = random.randint(0, length - 1)
            shuffle_deck.append(self.deck[select_random_num])
            length -= 1
            del self.deck[select_random_num]
            
        self.deck = shuffle_deck

    def draw(self, player_hand):
        if len(self.deck) != 0:
            top_card = self.deck.pop()
            
            player_hand.update_hand(top_card)
            player_hand.num_in_hand += 1
            
            return top_card

    def display_deck_count(self):
        print(f" Remaining cards in deck: {len(self.deck)}")

# punishing the player

    def remove_cards(self, amount):
        if amount == 0:
            return
        if amount > self.get_deck_count():
            self.deck = []
            return self.deck
        i = 0
        while i < amount:
            self.deck.pop()
            print("\n" + shredded_from_deck[random.randint(0, len(shredded_from_deck) -1)])
            i += 1
        

    
