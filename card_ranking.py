
from collections import defaultdict


class RankAgent(object):

    def __init__(self, cards):
        self.cards = cards

    def get_card_rank(self):
        card_rank = -1

        if self.is_high():
            card_rank = 0
        if self.is_pair():
            card_rank = 1

        return card_rank

    def is_high(self):
        return False

    def is_pair(self):
        return False

    def is_drill(self):
        
        for key in card_count_map.keys():
            if card_count_map[key] == 3:
                return True

        return False

    def _get_card_count_map(self):
        card_count_map = dict()
        for card in self.cards:
            card_count_map[card['rank']] = card_count_map.get(card_rank['rank'], 0) + 1

        return card_count_map

