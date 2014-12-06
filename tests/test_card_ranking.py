
from unittest import TestCase
from player import get_hole_card_ranks


class HoleCardsTestCase(TestCase):

    def setUp(self):
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
            ]
        }

    def test_hole_cards_are_fine(self):
        hole_card_ranks = get_hole_card_ranks(self.mock_game_state_ok)
        assert "A" in hole_card_ranks
        assert "K" in hole_card_ranks
