
from random import randint

"""
a hand
get_hand == shows current hand
get_draw == takes a card from the deck
play card
"""

class Player:
    def __init__(self):
        self.hand = []
        self.num_in_hand = 0


    def get_hand(self):
        return self.hand


    def get_hand_count(self):
        return len(self.hand)


    def display_hand(self):
        display_cards = []
        for card in self.hand:
            display_cards.append(card.get_card())

        print(" ".join(display_cards))

# playing card

    def is_card_in_hand(self, player_card):
        for card in self.hand:
            if card.get_card() == player_card.lower():
                return True
        
        return False

    def played_card(self, player_card):
        for i, card in enumerate(self.hand):
            if card.get_card() == player_card:
                return card

    def remove_card(self, player_card):
        for i, card in enumerate(self.hand):
            if card.get_card() == player_card:
                del self.hand[i]
                break


    def update_hand(self, card):
        self.hand.append(card)
        self.num_in_hand += 1

# punishing the player

    def is_max_hand(self):
        if self.get_hand_count() == 11:
            return True

    def remove_random_card(self):
        random_num = randint(0, self.get_hand_count() - 1)
        removed_card = self.hand[random_num]
        del self.hand[random_num]
        return removed_card


    


