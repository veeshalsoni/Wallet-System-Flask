from flask_restful import Resource, reqparse, abort
from flask import request
from src.enum import WalletType
from src.services.transaction_service import TransactionService, InsufficientFund
from src.services.user_service import UserService, WalletDoesNotExist


class DebitAmountResource(Resource):
    def post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument("wallet_type", type=str, required=True)
        parser.add_argument("amount", type=float, required=True)
        return parser

    def post(self):
        args = self.post_parser().parse_args()
        wallet_type = args["wallet_type"]
        amount = float(args["amount"])
        
        try:
            wallet_type = WalletType(wallet_type)
        except:
            return "Invalid Wallet Type"

        try:
            TransactionService.debit(wallet_type=wallet_type, amount=amount)
        except InsufficientFund:
            abort(400, message=f"Insufficient fund in your {wallet_type.value} wallet")
        except WalletDoesNotExist:
            abort(400, message=f"Wallet type {wallet_type.value} does not exist for the user")
    
        balance = UserService.get_wallet_balance(wallet_type)
        return {"balance": balance}


class CreditAmountResource(Resource):
    def post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument("wallet_type", type=str, required=True)
        parser.add_argument("amount", type=float, required=True)
        return parser

    def post(self):
        args = self.post_parser().parse_args()
        wallet_type = args["wallet_type"]
        amount = float(args["amount"])
        
        try:
            wallet_type = WalletType(wallet_type)
        except:
            return "Invalid Wallet Type"

        try:
            TransactionService.credit(wallet_type=wallet_type, amount=amount)
        except WalletDoesNotExist:
            abort(f"Wallet type {wallet_type.value} does not exist for the user")
    
        balance = UserService.get_wallet_balance(wallet_type)
        return {"balance": balance}


class UserTransactionsResource(Resource):
    # def get_parser(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("start_date", type=str, required=True)
    #     parser.add_argument("end_date", type=str, required=True)
    #     parser.add_argument("wallet_type", type=str, required=True)

    #     return parser
    
    def get(self):
        # args = self.get_parser().parse_args()
        # start_date = args["start_date"]
        # end_date = args["end_date"]
        # wallet_type = args["wallet_type"]

        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        wallet_type = request.args.get('wallet_type')        

        try:
            wallet_type = WalletType(wallet_type)
        except:
            return "Invalid Wallet Type"

        try:
            history = TransactionService.history(wallet_type=wallet_type, start_date=start_date, end_date=end_date)
        except WalletDoesNotExist:
            abort(f"Wallet type {wallet_type.value} does not exist for the user")
    
        return history
