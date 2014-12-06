

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
