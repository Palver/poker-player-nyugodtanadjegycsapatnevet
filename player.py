def have_high_cards(my_cards):
    return "A" in my_cards or "K" in my_cards


class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        offer = 100
        my_cards = get_hole_card_ranks(game_state)

        if have_high_cards(my_cards):
            offer = 1000
        card_values = {"A": 100,
                       "K": 50,
                       "Q": 40}


        return offer

    def showdown(self, game_state):
        pass


def get_hole_card_ranks(game_state):
    player_id = game_state['in_action']
    cards = game_state['players'][player_id]['hole_cards']
    return [card['rank'] for card in cards]
