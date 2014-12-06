
from helpers import get_hole_card_ranks, have_high_cards


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        offer = 100
        my_cards = get_hole_card_ranks(game_state)

        if have_high_cards(my_cards):
            offer = 1000
        card_values = {"A": 100,
                       "K": 50,
                       "Q": 40}


        return offer

    def showdown(self, game_state):
        pass
