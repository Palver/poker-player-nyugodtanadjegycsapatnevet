
class Player:
    VERSION = "ALL IN + some hole card stuff"

    def betRequest(self, game_state):
        return 1000

    def showdown(self, game_state):
        pass


def get_hole_card_ranks(game_state):
    player_id = game_state['in_action']
    cards = game_state['players'][player_id]['hole_cards']
    return [card['rank'] for card in cards]
