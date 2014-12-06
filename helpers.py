
def have_high_cards(my_cards):
    return "A" in my_cards or "K" in my_cards


def get_hole_card_ranks(game_state):
    player_id = game_state['in_action']
    cards = game_state['players'][player_id]['hole_cards']
    return [card['rank'] for card in cards]
