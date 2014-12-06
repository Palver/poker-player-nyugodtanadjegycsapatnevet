
from helpers import *
from card_ranking import RankAgent


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        my_cards = get_hole_card_ranks(game_state)
        all_cards = get_all_cards(game_state)
        myself = get_myself(game_state)
        current_cash = int(myself["stack"])

        ra = RankAgent(all_cards)
        rank = ra.get_card_rank()
        offer = 0

        if player_count(game_state) > 2 and rank < 4:
            offer = 0
        else:
            minimal_amount = int(game_state["minimum_raise"])
            if is_preflop(game_state):
                if ra._is_high() and is_well_positioned(game_state):
                    offer = minimal_amount
                elif ra._is_pair() and ra._is_high(8):
                    offer = max(current_cash * 0.25, minimal_amount)
            elif rank >= 5:
                offer = current_cash
            else:
                offer = minimal_amount * (1 + rank * 0.1)

        return offer

    def showdown(self, game_state):
        pass
