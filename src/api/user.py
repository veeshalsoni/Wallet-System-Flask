from flask_restful import Resource, reqparse, abort
from src.services.user_service import UserService, UserNotLoggedIn, UserAlreadyExist, UserDoesNotExist
from src.enum import WalletType


class UserCreationResource(Resource):
    def post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        return parser

    def post(self):
        args = self.post_parser().parse_args()
        username = args["username"]
        
        try:
            user = UserService.create_user(username)
        except UserAlreadyExist:
            abort(400, message=f"{username} already exists")
        except:
            abort(500, message="Server error, please try after sometime")
        return {"user": user.phone}


class LogInUser(Resource):
    def post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True)
        return parser

    def post(self):
        args = self.post_parser().parse_args()
        username = args["username"]
        
        try:
            user = UserService.authenticate(username)
        except UserDoesNotExist:
            abort(400, message="User does not exists")

        return {"user": user.phone}


class LogoutUser(Resource):
    def delete(self):
        UserService.deauthenticate()
        return "Success"


class CurrentUserResource(Resource):
    def get(self):
        try:
            user = UserService.get_current()
        except UserNotLoggedIn:
            return "User Is Not Logged In"
    
        return {"user": user.phone}


class CurrentUserBalanceResource(Resource):
    def get(self):
        wallets = UserService.get_wallet_balances()
        return wallets


class CreateWalletResource(Resource):
    def post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument("wallet_type", type=str, required=True)
        return parser

    def post(self):
        args = self.post_parser().parse_args()
        wallet_type = args["wallet_type"]

        try:
            wallet_type = WalletType(wallet_type)
        except:
            return "Invalid Wallet Type"

        wallet = UserService.create_wallet(wallet_type=wallet_type)
        return {"name": wallet.name, "balance": wallet.balance}


class GetWalletBalanceResource(Resource):
    def get(self, wallet_type):
        try:
            wallet_type = WalletType(wallet_type)
        except:
            return "Invalid Wallet Type"

        wallet = UserService.get_wallet_balance(wallet_type=wallet_type)
        return {"balance": wallet.balance}


class GetWalletTypeResource(Resource):
    def get(self):
        wallets = [wallet.value for wallet in WalletType]
        return wallets
