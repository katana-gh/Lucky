
#from player import Player
#from deck import Deck


class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num

    def get_color(self):
        return self.color

    def get_number(self):
        return self.num


    def get_card(self):
        return f"{self.get_color()} {self.get_number()}"


    def is_comparable(self, facing_card_obj):
        if self.color == facing_card_obj.color:
            
            return True
        if self.num == facing_card_obj.num:
            
            return True
        return False





