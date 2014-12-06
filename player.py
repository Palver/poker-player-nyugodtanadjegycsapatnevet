
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

        if player_count(game_state) > 2:
            offer = 0
        else:
            minimal_amount = int(game_state["minimum_raise"])
            if is_preflop(game_state):
                if ra._is_high() and is_well_positioned(game_state):
                    offer = minimal_amount

                if ra._is_pair() and ra._is_high(8):
                    offer = max(current_cash * 0.25, minimal_amount)
                if rank >= 5:
                    offer = max(current_cash * 0.5, minimal_amount)
            else:
                if rank == 0:
                    pass
                elif rank > 0 and rank < 5:
                    offer = max(minimal_amount, current_cash * 0.1)
                else:
                    offer = current_cash

        return int(offer)

    def showdown(self, game_state):
        pass
