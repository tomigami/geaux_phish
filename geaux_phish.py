import random


class Game:
    def __init__(self):
        self.draw_pile = list()
        self.discard_pile = list()
        self.player_one = Player(name="Brad")
        self.player_two = Player(name="Tom")

    def populate_draw_pile(self):
        print "Populating draw_pile."
        for value in range(1, 14):
            for suit in ["S", "H", "C", "D"]:
                card = Card(value=value, suit=suit)
                self.draw_pile.append(card)

    def print_draw_pile(self):
        print "Printing draw_pile."
        for i, card in enumerate(self.draw_pile):
            if i % 13 == 0:
                print
            card.print_card()
        print
        print "Our draw_pile has {} cards.".format(len(self.draw_pile))
        print

    def shuffle_draw_pile(self):
        random.shuffle(self.draw_pile)
        print "Erryday I'm shufflin'."

    def play_game(self):
        print "Playing game."
        self.populate_draw_pile()
        self.shuffle_draw_pile()
        self.print_draw_pile()
        self.player_one.print_player()
        self.player_two.print_player()
        self.deal_cards()
        self.player_one.print_player()
        self.player_two.print_player()

    def deal_cards(self):
        for _ in range(7):
            card = self.draw_pile.pop()
            self.player_one.hand.append(card)
            card = self.draw_pile.pop()
            self.player_two.hand.append(card)
        self.print_draw_pile()


class Player:
    def __init__(self,name):
        self.hand = list()
        self.tableau = list()
        self.name = name

    def print_player(self):
        print "Printing hand for {}.".format(self.name)
        for card in self.hand:
            card.print_card()
        print

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def print_card(self):
        print str(self.value) + self.suit,


game = Game()
game.play_game()
