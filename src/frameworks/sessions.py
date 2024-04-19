from flask import session

class WalletSystemSession:
    @classmethod
    def login(cls, user_id):
        session['user_id'] = user_id
    
    @classmethod
    def logout(cls):
        session.clear()
    
    @classmethod
    def current(cls):
        return session.get('user_id')
