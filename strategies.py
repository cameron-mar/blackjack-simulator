from enum import Enum


class Move(Enum):
    Double = "Double"
    Hit = "Hit"
    Split = "Split"
    SplitDouble = "Split if Double After Split"
    Stand = "Stand"
    Surrender = "Surrender"


hard_totals = {
    17: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Stand,
        "8": Move.Stand,
        "9": Move.Stand,
        "10": Move.Stand,
        "A": Move.Stand
    },
    16: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Surrender,
        "10": Move.Surrender,
        "A": Move.Surrender
    },
    15: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Surrender,
        "A": Move.Hit
    },
    14: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    13: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    12: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    11: {
        "2": Move.Double,
        "3": Move.Double,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Double,
        "8": Move.Double,
        "9": Move.Double,
        "10": Move.Double,
        "A": Move.Double
    },
    10: {
        "2": Move.Double,
        "3": Move.Double,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Double,
        "8": Move.Double,
        "9": Move.Double,
        "10": Move.Hit,
        "A": Move.Hit
    },
    9: {
        "2": Move.Hit,
        "3": Move.Double,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    8: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Hit,
        "5": Move.Hit,
        "6": Move.Hit,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    }
}

soft_totals = {
    20: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Stand,
        "8": Move.Stand,
        "9": Move.Stand,
        "10": Move.Stand,
        "A": Move.Stand
    },
    19: {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Double,
        "7": Move.Stand,
        "8": Move.Stand,
        "9": Move.Stand,
        "10": Move.Stand,
        "A": Move.Stand
    },
    18: {
        "2": Move.Double,
        "3": Move.Double,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Stand,
        "8": Move.Stand,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    17: {
        "2": Move.Hit,
        "3": Move.Double,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    16: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    15: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Double,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    14: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Hit,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    13: {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Hit,
        "5": Move.Double,
        "6": Move.Double,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    }
}

splits = {
    "A": {
        "2": Move.Split,
        "3": Move.Split,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Split,
        "8": Move.Split,
        "9": Move.Split,
        "10": Move.Split,
        "A": Move.Split
    },
    "10": {
        "2": Move.Stand,
        "3": Move.Stand,
        "4": Move.Stand,
        "5": Move.Stand,
        "6": Move.Stand,
        "7": Move.Stand,
        "8": Move.Stand,
        "9": Move.Stand,
        "10": Move.Stand,
        "A": Move.Stand
    },
    "9": {
        "2": Move.Split,
        "3": Move.Split,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Stand,
        "8": Move.Split,
        "9": Move.Split,
        "10": Move.Stand,
        "A": Move.Stand
    },
    "8": {
        "2": Move.Split,
        "3": Move.Split,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Split,
        "8": Move.Split,
        "9": Move.Split,
        "10": Move.Split,
        "A": Move.Split
    },
    "7": {
        "2": Move.Split,
        "3": Move.Split,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Split,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    "6": {
        "2": Move.SplitDouble,
        "3": Move.Split,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    "5": {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Hit,
        "5": Move.Hit,
        "6": Move.Hit,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    "4": {
        "2": Move.Hit,
        "3": Move.Hit,
        "4": Move.Hit,
        "5": Move.SplitDouble,
        "6": Move.SplitDouble,
        "7": Move.Hit,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    "3": {
        "2": Move.SplitDouble,
        "3": Move.SplitDouble,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Split,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    },
    "2": {
        "2": Move.SplitDouble,
        "3": Move.SplitDouble,
        "4": Move.Split,
        "5": Move.Split,
        "6": Move.Split,
        "7": Move.Split,
        "8": Move.Hit,
        "9": Move.Hit,
        "10": Move.Hit,
        "A": Move.Hit
    }
}
