
from helpers import *
from card_ranking import RankAgent


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        my_cards = get_hole_card_ranks(game_state)
        all_cards = get_all_cards(game_state)
        myself = get_myself(game_state)

        ra = RankAgent(all_cards)
        rank = ra.get_card_rank()
        offer = 0

        if player_count(game_state) > 2 and rank < 4:
            offer = 0
        else:
            if is_preflop(game_state):
                if ra._is_high() and is_well_positioned(game_state):
                    offer = game_state["minimum_raise"]
                elif ra._is_pair() and ra._is_high(8):
                    offer = 1000
            elif rank >= 5:
                offer = int(myself["stack"])
            else:
                offer = int(game_state["minimum_raise"]) * rank * 1.1

        return offer

    def showdown(self, game_state):
        pass
