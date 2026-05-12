
"""
turn begins
turn ends
"""

class Turn:
    def __init__(self):
        self.turn = 0

    #def is_playable(self, player, card):    
    def get_turn(self):
        return self.turn

    def update_turn(self):
        self.turn += 1

    def display_turn(self):
        print(f"Turn: {self.turn}")





