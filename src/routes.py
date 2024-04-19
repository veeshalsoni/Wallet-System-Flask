from flask import render_template, Blueprint, redirect, url_for, request
from src.frameworks.sessions import WalletSystemSession

user_bp = Blueprint('user', __name__)


@user_bp.before_request
def check_login():
    user_logged_in = not not WalletSystemSession.current()
    print(request.path)
    if not user_logged_in and request.path in "/dashboard":
        # Redirect the user to the login page
        return redirect(url_for('user.login'))


@user_bp.route("/login")
def login():
    return render_template('login.html')


@user_bp.route("/signup")
def signup():
    return render_template("signup.html")


@user_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user_logged_in=True)


@user_bp.route("/")
def home():
    return redirect(url_for('user.dashboard'))


@user_bp.route('/logout')
def logout():
    WalletSystemSession.logout()
    return redirect(url_for('user.login'))
