
from unittest import TestCase
from player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player()
        self.mock_game_state_ok = {
            'in_action': 0,
            'players': [
                {
                    'hole_cards': [
                        {
                            'rank': "A"
                        },
                        {
                            'rank': "K"
                        }
                    ]
                }
            ],
            'community_cards': []
        }

    def test_player_returns_int(self):
        hopefully_int = self.player.betRequest(self.mock_game_state_ok)
        assert type(hopefully_int) == int
