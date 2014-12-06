
from helpers import *
from card_ranking import RankAgent


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        offer = 100
        my_cards = get_hole_card_ranks(game_state)
        all_cards = get_all_cards(game_state)

        ra = RankAgent(all_cards)
        rank = ra.get_card_rank()

        offer = rank * 50

        return offer

    def showdown(self, game_state):
        pass
