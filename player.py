
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

        if is_preflop(game_state):
            if ra._is_high():
                offer = game_state["minimum_raise"]
            elif ra._is_pair():
                offer = 1000
            # ha legalabb egy magas kartya, tartsuk
            # ha van magas parunk, all-in


        else:
            # a tobb jatekos van, es gyenge a lapunk => FOLD
            if rank in [1, 2] and player_count(game_state) > 2:
                offer = 0




        return offer

    def showdown(self, game_state):
        pass
