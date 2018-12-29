import random
import time

class Game:
    def __init__(self):
        self.draw_pile = list()
        self.discard_pile = list()
        self.player_one = Player(name="Brad")
        self.player_two = Player(name="Tom")
        self.setup_game()

    def setup_game(self):
        self.populate_draw_pile()
        self.shuffle_draw_pile()
        self.print_draw_pile()  # Print length instead?
        self.player_one.print_player()
        self.player_two.print_player()
        self.deal_cards()

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
        self.player_one.print_player()
        self.player_two.print_player()
        # self.player_one.draw_card(draw_pile=self.draw_pile)
        # self.player_two.draw_card(draw_pile=self.draw_pile)
        # self.print_draw_pile()
        # value=self.player_one.hand[4].value
        current_player=self.player_one
        other_player=self.player_two
        while True:
            card_index = 0
            current_player.request_card(
                other_player=other_player,
                card_index=card_index,
                draw_pile=self.draw_pile)
            time.sleep(1)
            current_player,other_player=other_player,current_player

    def deal_cards(self):
        for _ in range(7):
            card = self.draw_pile.pop()
            self.player_one.hand.append(card)
            card = self.draw_pile.pop()
            self.player_two.hand.append(card)
        self.print_draw_pile()


class Player:
    def __init__(self, name):
        self.hand = list()
        self.tableau = list()
        self.name = name

    def print_player(self):
        print "Printing hand for {}.".format(self.name)
        for card in self.hand:
            card.print_card()
        print

    def draw_card(self, draw_pile):
        card = draw_pile.pop()
        self.hand.append(card)
        print "Drawing card for {}.".format(self.name)

    def request_card(self, other_player, card_index, draw_pile):
        card = self.hand[card_index]
        possible_card = other_player.respond_to_request(requested_value=card.value)
        if possible_card is None:
            self.draw_card(draw_pile)
        else:
            self.hand.append(possible_card)

    def respond_to_request(self, requested_value):
        for i, card in enumerate(self.hand):
            if requested_value is card.value:
                print "I have your match."
                return self.hand.pop(i)
        print "Go fish."
        return None


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def print_card(self):
        print str(self.value) + self.suit,


game = Game()
game.play_game()
