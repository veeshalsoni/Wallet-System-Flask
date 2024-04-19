from enum import Enum

class WalletType(Enum):
    TRAVEL = "travel"
    FOOD = "food"
    GENERAL = "general"

    @classmethod
    def get_minimum_balance(cls, wallet_type):
        if wallet_type == cls.TRAVEL:
            return 0
        if wallet_type == cls.FOOD:
            return 0
        if wallet_type == cls.GENERAL:
            return 100
    
        return -1


class TransactionType(Enum):
    DEBIT = "debit"
    CREDIT = "credit"
