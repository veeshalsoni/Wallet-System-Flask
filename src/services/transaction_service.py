from datetime import datetime
from src.enum import TransactionType, WalletType
from src.services.user_service import UserService
from src.frameworks.db import wallet_db
from src.models.wallet import Wallet
from src.models.transactions import Transaction
from src.models.user import User


class InsufficientFund(Exception):
    pass


class TransactionService:
    @classmethod
    def _update_wallet(cls, wallet_record, transaction_type, amount):
        new_amount = 0
        if transaction_type == TransactionType.DEBIT:
            new_amount = wallet_record.balance - amount
        elif transaction_type == TransactionType.CREDIT:
            new_amount = wallet_record.balance + amount
        
        wallet_record.balance = new_amount
        wallet_record.save()
    
    @classmethod
    def _create_transaction(cls, wallet_record, transaction_type, amount):
        Transaction.create(amount=amount, type=transaction_type.value, wallet=wallet_record)

    @classmethod
    def debit(cls, wallet_type, amount):
        # to validate the wallet type
        wallet_type = WalletType(wallet_type)
        min_amount = WalletType.get_minimum_balance(wallet_type=wallet_type)

        with wallet_db.atomic():
            wallet_record = UserService.get_wallet(wallet_type=wallet_type)
        
            if wallet_record.balance - min_amount >= amount:
                cls._update_wallet(wallet_record, TransactionType.DEBIT, amount)
                cls._create_transaction(wallet_record, TransactionType.DEBIT, amount)
            else:
                raise InsufficientFund
        

        
    @classmethod
    def credit(cls, wallet_type, amount):
        # to validate the wallet type
        wallet_type = WalletType(wallet_type)

        with wallet_db.atomic():
            wallet_record = UserService.get_wallet(wallet_type=wallet_type)
            cls._update_wallet(wallet_record, TransactionType.CREDIT, amount)
            cls._create_transaction(wallet_record, TransactionType.CREDIT, amount)


    @classmethod
    def history(cls, wallet_type, start_date, end_date):
        cur_user = UserService.get_current()
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        wallet_records = Transaction.select() \
            .join(Wallet) \
            .join(User) \
            .where(
                User.phone == cur_user.phone,
                Wallet.name == wallet_type.value,
                Transaction.date >= start_date,
                Transaction.date <= end_date,
            )

        transactions = []
        for record in wallet_records:
            transactions.append({
                "type": record.type,
                "amount": record.amount,
                "date": datetime.strftime(record.date, "%d-%m-%Y")
            })
        
        return transactions
