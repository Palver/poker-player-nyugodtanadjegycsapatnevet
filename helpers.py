
def have_high_cards(my_cards):
    return "A" in my_cards or "K" in my_cards


def get_hole_card_ranks(game_state):
    player_id = game_state['in_action']
    cards = game_state['players'][player_id]['hole_cards']
    return [card['rank'] for card in cards]


def get_all_cards(game_state):
    player_id = game_state['in_action']
    all_cards = game_state['players'][player_id]['hole_cards']
    all_cards += game_state['community_cards']
    return all_cards


def get_player_count(game_state):
    return len(game_state["players"])


def is_preflop(game_state):
    return len(game_state["community_cards"]) == 0


def get_myself(game_state):
    player_id = game_state['in_action']
    return game_state['players'][player_id]


def is_well_positioned(game_state):
    player_id = game_state['in_action']
    dealer = game_state['dealer']
    
    is_last_seat = player_id == get_player_count(game_state) - 1
    is_dealer_seat = player_id == dealer

    return is_last_seat or is_dealer_seat
