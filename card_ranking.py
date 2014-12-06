
from collections import defaultdict


class RankAgent(object):

    def __init__(self, cards):
        self._rank2value = {"J": 11, "Q": 12, "K": 13, "A": 14}
        self._value2rank = {"11": "J", "12": "Q", "13": "K", "14": "A"}

        self.cards = cards
        self._card_rank_count = dict()
        self._card_suit_count = dict()
        self._card_values = list()
        self._count_cards()


    def get_card_rank(self):
        card_rank = 0

        if self._is_pair():
            card_rank = 1
        if self._is_two_pairs():
            card_rank = 2
        if self._is_drill():
            card_rank = 3
        if self._is_straight():
            card_rank = 4
        if self._is_flush():
            card_rank = 5
        if self._is_full_house():
            card_rank = 10
        if self._is_poker():
            card_rank = 10

        return card_rank

    def _is_high(self, min_value=13):
        highest_card = max(self._card_values)

        if highest_card >= min_value:
            return True

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

    def _is_series(self, unique_card_ranks):
        if len(unique_card_ranks) < 5:
            return False

        if float(unique_card_ranks[2]) == self.__average(unique_card_ranks):
            first, second, third = unique_card_ranks[:3]
            if first + 1 == second and second + 1 == third:
                return True
        return False


    def _is_straight(self):
        unique_card_ranks = sorted(self._card_values)

        series_5 = self._is_series(unique_card_ranks[0:5])
        if len(unique_card_ranks) == 5:
            return series_5
        series_6 = self._is_series(unique_card_ranks[1:6])
        if len(unique_card_ranks) == 6:
            return series_5 or series_6
        series_7 = self._is_series(unique_card_ranks[2:7])
        return series_5 or series_6 or series_7


    def __average(self, values):
        return float(sum(values) / len(values))


    def _count_cards(self):
        for card in self.cards:
            rank = card['rank']
            suit = card['suit']
            self._card_rank_count[rank] = self._card_rank_count.get(rank, 0) + 1
            self._card_suit_count[suit] = self._card_suit_count.get(suit, 0) + 1
            self._card_values.append(self._value_from_rank(rank))


    def _value_from_rank(self, rank):
        rank = str(rank)
        if rank.isdigit():
            return int(rank)
        else:
            return self._rank2value[rank]