from enums import FaceCards, Move

def check_variations(
        dealer_card: str, player_total: int, true_count: float):
    """player totals has to be a hard total.
    Returns a Move
    """
    if dealer_card == FaceCards.ACE:
        return Move.Insurance
    if player_total == 16:
        if dealer_card == "8" and true_count >= 4.0:
            return Move.Surrender
        if dealer_card == "9" and true_count <= -1.0:
            return Move.Surrender
        if dealer_card in FaceCards.get_ten_cards() and true_count <= -1.0:
            return Move.Surrender
        if dealer_card == FaceCards.ACE and true_count == 0:
            return Move.Surrender
    if player_total == 15:
        if dealer_card == "8" and true_count >= 7.0:
            return Move.Surrender
        if dealer_card == "9" and true_count >= 2.0:
            return Move.Surrender
        if dealer_card in FaceCards.get_ten_cards() and true_count == 0:
            return Move.Surrender
        if dealer_card == FaceCards.ACE and true_count >= 2.0:
            return Move.Surrender
    if player_total == 14:
        if dealer_card == "9" and true_count >= 7.0:
            return Move.Surrender
        if dealer_card in FaceCards.get_ten_cards() and true_count >= 3.0:
            return Move.Surrender
        if dealer_card == FaceCards.ACE and true_count >= 5.0:
            return Move.Surrender
    if player_total == 13:
        if dealer_card in FaceCards.get_ten_cards() and true_count >= 8.0:
            return Move.Surrender