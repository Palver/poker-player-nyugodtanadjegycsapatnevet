
from collections import defaultdict


class RankAgent(object):

    def __init__(self, cards):
        self.cards = cards
        self._card_rank_count = dict()
        self._card_suit_count = dict()
        self._count_cards()

    def get_card_rank(self):
        card_rank = 0

        if self._is_pair():
            card_rank = 1
        if self._is_two_pairs():
            card_rank = 2
        if self._is_drill():
            card_rank = 3
        if self._is_flush():
            card_rank = 4
        if self._is_full_house():
            card_rank = 5
        if self._is_poker():
            card_rank = 10

        return card_rank

    def is_high(self):
        return False

    def _is_pair(self):
        return 2 in self._card_rank_count.values()

    def _is_drill(self):
        return 3 in self._card_rank_count.values()

    def _is_two_pairs(self):
        count_list = list(self._card_rank_count.values())
        number_of_pairs = count_list.count(2)
        return 2 == number_of_pairs

    def _is_flush(self):
        return max(self._card_suit_count.values()) >= 5

    def _is_full_house(self):
        return self._is_pair() and self._is_drill()

    def _is_poker(self):
        return 4 in self._card_rank_count.values()

    def _count_cards(self):
        for card in self.cards:
            rank = card['rank']
            suit = card['suit']
            self._card_rank_count[rank] = self._card_rank_count.get(rank, 0) + 1
            self._card_suit_count[suit] = self._card_suit_count.get(suit, 0) + 1



