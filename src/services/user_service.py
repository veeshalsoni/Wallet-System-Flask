from src.frameworks.sessions import WalletSystemSession
from src.models.user import User
from src.models.wallet import Wallet

class UserDoesNotExist(Exception):
    pass


class UserAlreadyExist(Exception):
    pass


class UserNotLoggedIn(Exception):
    pass


class WalletDoesNotExist(Exception):
    pass


class UserService:
    @classmethod
    def create_user(cls, username):
        user = User.get_or_none(phone=username)
        if user:
            raise UserAlreadyExist

        user = User.create(phone=username)
        return user

    @classmethod
    def authenticate(cls, username):
        user = User.get_or_none(phone=username)
        if not user:
            raise UserDoesNotExist
    
        WalletSystemSession.login(user_id=username)
        return user
    
    @classmethod
    def deauthenticate(cls):    
        WalletSystemSession.logout()
    
    @classmethod
    def get_current(cls):
        current = WalletSystemSession.current()
        if not current:
            raise UserNotLoggedIn
    
        user = User.get_or_none(phone=current)
        return user

    @classmethod
    def create_wallet(cls, wallet_type):
        current_user = cls.get_current()
        wallet = Wallet.get_or_none(Wallet.user == current_user, Wallet.name == wallet_type.value)
        if wallet:
            return wallet

        wallet =  Wallet.create(user=current_user, name=wallet_type.value)
        return wallet

    @classmethod
    def get_wallet_balance(cls, wallet_type):
        wallet = cls.get_wallet(wallet_type)
        return wallet.balance

    @classmethod
    def get_wallet(cls, wallet_type):
        current_user = cls.get_current()
        wallet = Wallet.get_or_none(Wallet.user == current_user, Wallet.name == wallet_type.value)
        if not wallet:
            raise WalletDoesNotExist
    
        return wallet

    @classmethod
    def get_wallet_balances(cls):
        current_user = cls.get_current()
        wallets = {}
        for wallet in current_user.wallets:
            wallets[wallet.name] = wallet.balance
        
        return wallets
