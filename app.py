import random
from enums import FaceCards
from strategies import hard_totals, soft_totals, splits

CARDS = [FaceCards.ACE, FaceCards.KING, FaceCards.QUEEN, FaceCards.JACK,
         "10", "9", "8", "7", "6", "5", "4", "3", "2"]
DECK_SIZE = 52
NUMBER_OF_DECKS = 8


def calculate_aces(number_of_aces, total):
    """Adds aces to the total"""
    new_total = total

    if new_total <= 11 - number_of_aces:
        new_total += 10 + number_of_aces
    else:
        new_total += number_of_aces
    
    return new_total


def calculate_cards(cards: list):
    aces = 0
    hand_value = 0
    for card in cards:
        try:
            hand_value += int(card)
        except ValueError:
            # face card
            if card != FaceCards.ACE:
                hand_value += 10
            else:
                aces += 1
    if aces > 0:
        return calculate_aces(aces, hand_value)

    return hand_value


def construct_deck():
    one_deck = CARDS * 4
    shoe = NUMBER_OF_DECKS * one_deck
    random.shuffle(shoe)
    return shoe


def deal_card(deck: list):
    return deck.pop(0)


def determine_correct_opening_move(
        dealer_card: str, player_cards: list,
        running_count: int, true_count: float):
    """Assumes there are only two cards in player hand"""

    if player_cards[0] == player_cards[1]:
        return splits[player_cards[0]][dealer_card]

    first_card = player_cards


def determine_soft_or_hard_total(cards: list):
    total = calculate_cards(cards)
    if FaceCards.ACE in cards:
        return "soft"


def display_dealer_opening_hand(hand: list):
    return hand[0]


def display_hand(hand: list, user: str):
    hand_string = f"{user} hand: "
    for card in hand:
        hand_string += f"{str(card)} "
    return hand_string


def get_true_count(running_count: int, shoe_size: int) -> float:
    remaining_decks = round(float(shoe_size) / float(DECK_SIZE) * 2.0) / 2.0
    true_count = round(float(running_count)/remaining_decks * 2.0) / 2.0
    return true_count


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
    while True:
        player_cards = []
        dealer_cards = []
        shoe_size = len(shoe)
        true_count = get_true_count(running_count, shoe_size)
        # Check if user wants to continue playing once deck gets to here
        if shoe_size < DECK_SIZE:
            continue_play = input("Continue playing? ")
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
            player_cards + [dealer_cards[1]], running_count)

        print(display_hand(player_cards, "player"))
        print(display_dealer_opening_hand(dealer_cards))

        determine_correct_move(
            dealer_cards[1], player_cards, running_count, true_count)

        player_decision = input("Hit, Double, Split, or Stand? ")


if __name__ == "__main__":
    shoe = construct_deck()
    run_game(shoe)
