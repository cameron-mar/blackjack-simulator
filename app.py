import random
from strategies import hard_totals, soft_totals, splits

CARDS = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
DECK_SIZE = 52
NUMBER_OF_DECKS = 8


def construct_deck():
    one_deck = CARDS * 4
    return shuffle_deck(NUMBER_OF_DECKS * one_deck)


def deal_card(deck: list):
    return deck.pop(0)


def display_player_hand(hand: list):
    hand_string = ""
    for card in hand:
        hand_string += f"{str(card)} "
    return hand_string


def shuffle_deck(deck: list):
    return random.shuffle(deck)


def update_running_count(cards: list, running_count: int):
    for card in cards:
        if isinstance(card, str):
            running_count -= 1
        if isinstance(card, int):
            if card < 7:
                running_count += 1
            if card == 10:
                running_count -= 1
    return running_count


def run_game(shoe: list):
    running_count = 0
    true_count = running_count / NUMBER_OF_DECKS
    while True:
        player_cards = []
        dealer_cards = []
        shoe_size = len(shoe)
        # Check if user wants to continue playing once deck gets to here
        if shoe_size < DECK_SIZE:
            continue_play = input("Continue playing?")
            if continue_play:
                shoe = construct_deck()
                continue
            else:
                return

        # Deal cards
        player_cards.append(deal_card(shoe))
        dealer_cards.append(deal_card(shoe))
        player_cards.append(deal_card(shoe))
        dealer_cards.append(deal_card(shoe))

        # Update running count with current cards and dealer's first card
        running_count = update_running_count(
            player_cards + dealer_cards[1], running_count)


if __name__ == "main":
    shoe = construct_deck()
    run_game(shoe)
