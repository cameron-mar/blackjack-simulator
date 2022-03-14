import app
import unittest

class TestApp(unittest.TestCase):


# -----------------------------------------------------------------------------
# calculate_aces tests

    def test_calculate_aces_one_ace_total_10_or_less(self):
        for x in range(1, 11):
            total = app.calculate_aces(1, x)

            self.assertEqual(total, x + 11)

    def test_calculate_aces_one_ace_total_11_or_more(self):
        for x in range(11, 22):
            total = app.calculate_aces(1, x)

            self.assertEqual(total, x + 1)

    def test_calculate_aces_two_aces_total_9_or_less(self):
        for x in range(1, 10):
            total = app.calculate_aces(2, x)

            self.assertEqual(total, x + 12)

    def test_calculate_aces_two_aces_total_10_or_more(self):
        """Tests when the total is 10 or more"""
        for x in range(10, 22):
            total = app.calculate_aces(2, x)

            self.assertEqual(total, x + 2)

# -----------------------------------------------------------------------------
# deal_card tests
    def test_deal_card(self):
        deck = ["a", "b", "c"]
        first_card = deck[0]
        remaining_deck = deck[1:]

        card = app.deal_card(deck)

        self.assertEqual(first_card, card)
        self.assertEqual(deck, remaining_deck)

# -----------------------------------------------------------------------------
# get_true_count tests

    def test_get_true_count(self):
        running_count = 2
        shoe_size = 104
        expected_true_count = 1

        true_count = app.get_true_count(running_count, shoe_size)
        
        self.assertEqual(true_count, expected_true_count)

    def test_get_true_count_half(self):
        running_count = 2
        shoe_size = 78
        expected_true_count = 1.5

        true_count = app.get_true_count(running_count, shoe_size)
        
        self.assertEqual(true_count, expected_true_count)

    def test_get_true_count_near_half(self):
        running_count = 2
        shoe_size = 80
        expected_true_count = 1.5

        true_count = app.get_true_count(running_count, shoe_size)
        
        self.assertEqual(true_count, expected_true_count)

    
    def test_get_true_count_running_odd_shoe_half(self):
        running_count = 3
        shoe_size = 80
        expected_true_count = 2

        true_count = app.get_true_count(running_count, shoe_size)
        
        self.assertEqual(true_count, expected_true_count)

    
    def test_get_true_count_running_negative(self):
        running_count = -3
        shoe_size = 80
        expected_true_count = -2

        true_count = app.get_true_count(running_count, shoe_size)
        
        self.assertEqual(true_count, expected_true_count)


# -----------------------------------------------------------------------------
# update_running_count tests

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
