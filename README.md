# Python Fundamentals & Object-Oriented Programming (OOP) – From Basics to Advanced

This repository contains a variety of Python exercises that I have completed during my studies, from basic syntax and data structures to more advanced concepts like Object-Oriented Programming (OOP). The goal is to demonstrate my growth and understanding of Python and show how I've applied it in real-world-like scenarios.

## Table of Contents

- [Basic Python Exercises](#basic-python-exercises)
- [Object-Oriented Programming (OOP) Examples](#object-oriented-programming-oop-examples)
- [Bank Account Class Example](#bank-account-class-example)
- [How to Contribute](#how-to-contribute)
- Emanuel Restrepo
  -+55 2196529 2925 | emadavresgar@icloud.com |
  -https://www.linkedin.com/in/emanuelrestrepo/

## Basic Python Exercises

This section includes beginner-level exercises focused on variables, data types, loops, conditionals, and basic functions.

## Object-Oriented Programming (OOP) Examples

This section showcases my understanding of OOP principles such as classes, inheritance, polymorphism, encapsulation, and abstraction.

## Bank Account Class Example

The following Python code demonstrates the creation of a `BankAccount` class, which includes basic functionalities such as depositing money, withdrawing funds, transferring between accounts, and checking account status.

```python
# Bank Account Class Implementation

class BankAccount:
    def __init__(self, number, name):
        self.account = number
        self.owner = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient funds")

    def check_balance(self):
        if self.balance >= 0:
            print("Balance is positive")
        else:
            print("Balance is negative")

    def display_account_info(self):
        print(f"{self.owner}, account {self.account}, has a balance of ${self.balance}")

# Main program
account1 = BankAccount(123, "Juan Perez")
account2 = BankAccount(456, "Roberto Gómez")

account1.deposit(1000)
account1.withdraw(1250)
account1.display_account_info()
account1.check_balance()

account2.deposit(3500)
account2.withdraw(1800)
account2.display_account_info()
account2.check_balance()

account2.transfer(account1, 600)
account1.display_account_info()
account1.check_balance()
account2.display_account_info()
account2.check_balance()



## Overview

### Key Points:
- **Title and Description**: They highlight both the beginner and advanced stages of the repository and your intent to keep improving.
- **Code Example**: The Bank Account code example demonstrates your knowledge of OOP principles, like classes, methods, and basic logic.
- **Structure**: The Markdown file is structured with sections to make it easy for recruiters to navigate and understand the content.
- **Future Updates**: The repository will continue to grow with more advanced projects and improvements.

These points summarize the overall structure and purpose of the repository and serve as a roadmap for your ongoing work.

