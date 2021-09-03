import app
import unittest

class TestApp(unittest.TestCase):

    def test_deal_card(self):
        deck = ["a", "b", "c"]
        first_card = deck[0]
        remaining_deck = deck[1:]

        card = app.deal_card(deck)

        self.assertEqual(first_card, card)
        self.assertEqual(deck, remaining_deck)

    def test_shuffle_deck(self):
        deck = ["a", "b", "c", "d"]
        shuffled_deck = app.shuffle_deck(deck)
        self.assertNotEqual(deck, shuffled_deck)

    def test_update_running_count(self):
        expected_results = {
            -2: ["A", "K", 7, 9],
            0: ["A", 10, 9, 7, 6, 2],
            2: [2, 7, 8, 9, 10, 3, 4]
        }
        for expected_count, cards in expected_results.items():
            new_running_count = app.update_running_count(
                cards, 0)
            self.assertEqual(
                expected_count, new_running_count)
