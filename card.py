
COLOR = ["blue", "green", "red", "yellow"]
NUM = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num

    def card_color(self):
        return self.color

    def card_num(self):
        return self.num
