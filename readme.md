# Wallet System

## Features

- **Login**: Users can log in using their phone numbers.
- **Signup**: New users can sign up with their phone numbers.
- **Wallet Creation**: Users can create wallet types by clicking on the "Wallet" button.
- **Dashboard**: Upon logging in, users are directed to the dashboard where they can view their wallet balances and perform transactions.

## Getting Started

### Prerequisites

- Python 3
- Flask
- SQLite

### Installation

1. Clone the repository:
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask application:
```
python runserver.py
```
4. Access the application in your web browser: http://0.0.0.0:5000/signup

## Docker version

``` 
docker build -t wallet-system .
docker run -p 5000:5000 wallet-system
```

Access the application in your web browser: http://0.0.0.0:5000/signup