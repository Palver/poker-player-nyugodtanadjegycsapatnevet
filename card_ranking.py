
from collections import defaultdict


class RankAgent(object):


    def __init__(self, cards):
        self.cards = cards
        self._card_count = dict()
        self._count_cards()

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
        return 2 in self._card_count.values()

    def is_drill(self):
        return 3 in self._card_count.values()

    def is_two_pair(self):
        count_list = list(self._card_count.values())
        number_of_pairs = count_list.count(2)
        return 2 == number_of_pairs

    def _count_cards(self):
        for card in self.cards:
            rank = card['rank']
            self._card_count[rank] = self._card_count.get(rank, 0) + 1

