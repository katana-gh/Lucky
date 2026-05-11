
#from card import Card

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

    def display_hand(self):
        display_cards = []
        for card in self.hand:
            display_cards.append(card.get_card())
        print(display_cards)

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








