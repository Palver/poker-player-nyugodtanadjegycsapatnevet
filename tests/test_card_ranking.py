
from unittest import TestCase
from helpers import get_hole_card_ranks
from card_ranking import RankAgent


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


class RankingAgentTestCase(TestCase):

    def setUp(self):
        self.mock_2_cards_no_pair = [{'rank': 'A', 'suit': 'spades'}, {'rank': 'K', 'suit': 'spades'}]
        self.mock_3_cards_no_pair = [{'rank': 'A', 'suit': 'spades'}, {'rank': 'K', 'suit': 'spades'}, {'rank': 'Q', 'suit': 'spades'}]
        self.mock_3_cards_drill = [{'rank': 'A', 'suit': 'spades'}, {'rank': 'A', 'suit': 'hearts'}, {'rank': 'A', 'suit': 'spades'}]

    def test_is_drill_is_false(self):
        self.ranking_agent = RankAgent(self.mock_2_cards_no_pair)
        assert not self.ranking_agent._is_drill()

        self.ranking_agent = RankAgent(self.mock_3_cards_no_pair)
        assert not self.ranking_agent._is_drill()

    def test_is_drill_is_true(self):
        self.ranking_agent = RankAgent(self.mock_3_cards_drill)
        assert self.ranking_agent._is_drill()


