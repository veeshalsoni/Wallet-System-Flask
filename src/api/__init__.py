from src.api.user import UserCreationResource, CurrentUserResource, CurrentUserBalanceResource, CreateWalletResource, GetWalletBalanceResource, LogInUser, LogoutUser, GetWalletTypeResource
from src.api.transaction import DebitAmountResource, CreditAmountResource, UserTransactionsResource


def register_resources(api):
    api.add_resource(UserCreationResource, "/api/user")
    api.add_resource(LogInUser, "/api/login")
    api.add_resource(LogoutUser, "/api/logout")
    api.add_resource(CurrentUserResource, "/api/user/me")
    api.add_resource(CurrentUserBalanceResource, "/api/user/me/balance")
    api.add_resource(CreateWalletResource, "/api/user/me/wallet")
    api.add_resource(GetWalletBalanceResource, "/api/user/me/wallet/<string:wallet_type>/balance")
    api.add_resource(GetWalletTypeResource, "/api/wallets")


    api.add_resource(DebitAmountResource, "/api/transaction/debit")
    api.add_resource(CreditAmountResource, "/api/transaction/credit")
    api.add_resource(UserTransactionsResource, "/api/transactions")
