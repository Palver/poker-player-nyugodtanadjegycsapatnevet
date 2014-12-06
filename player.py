
from helpers import *
from card_ranking import RankAgent


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        my_cards = get_hole_card_ranks(game_state)
        all_cards = get_all_cards(game_state)

        ra = RankAgent(all_cards)
        rank = ra.get_card_rank()
        offer = 50 * rank

        if rank in [1, 2] and player_count(game_state) > 2:
            offer = 0

        return offer

    def showdown(self, game_state):
        pass
