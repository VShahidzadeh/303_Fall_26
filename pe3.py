# Pair Exercise #3: Functions and Classes
# Varuzhan Shahidzadeh, Partner: Daniel Abalusi

import string
import datetime


# ---------------------------------------------------------------
# Functions: Caesar cipher
# ---------------------------------------------------------------

def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded = ""
    for char in input_text:
        lower = char.lower()
        if lower in alphabet:
            index = alphabet.index(lower)          
            new_index = (index + shift) % 26       
            encoded += alphabet[new_index]
        else:
            encoded += char                        
    return (alphabet, encoded)

def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded = ""
    for char in input_text:
        lower = char.lower()
        if lower in alphabet:
            decoded += alphabet[(alphabet.index(lower) - shift) % 26]
        else:
            decoded += char
    return decoded


# ---------------------------------------------------------------
# Classes
# ---------------------------------------------------------------

class BankAccount:
    def __init__(self, name="Rainy", ID="1234",
                 creation_date=datetime.date.today(), balance=0):
                if creation_date > datetime.date.today():
                    raise Exception("Creation date cannot be in the future")
                self.name = name
                self.ID = ID
                self.creation_date = creation_date
                self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative")
        else:
            self.balance += amount
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount cannot be negative")
        else:
            self.balance -= amount
        print(f"Balance: ${self.balance}")

    def view_balance(self):
        print(f"Balance: ${self.balance}")
        return self.balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        age_in_days = (datetime.date.today() - self.creation_date).days
        if age_in_days < 180:
            print("Withdrawals are not allowed until the account is 180 days old")
        elif amount > self.balance:
            print("Insufficient funds: overdrafts are not allowed on savings accounts")
        else:
            self.balance -= amount
        print(f"Balance: ${self.balance}")


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 30
        print(f"Balance: ${self.balance}")      