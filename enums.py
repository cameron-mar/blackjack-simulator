from enum import Enum

class FaceCards(Enum):
    ACE = "A"
    KING = "K"
    QUEEN = "Q"
    JACK = "J"

    @classmethod
    def get_all():
        return [card.value for card in FaceCards]

    @classmethod
    def get_ten_cards():
        return [FaceCards.KING, FaceCards.QUEEN, FaceCards.JACK]

class Move(Enum):
    Double = "Double"
    Hit = "Hit"
    Insurance = "Insurance"
    Split = "Split"
    SplitDouble = "Split if Double After Split"
    Stand = "Stand"
    Surrender = "Surrender"