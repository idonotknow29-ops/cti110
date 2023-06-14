Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # A program to calculate the remainind funds left after travel expenses
>>> # 6/14/23
>>> # CTI-110 P1HW2 - Travel expense
>>> # Matthew Dean
>>> #
>>> print('This program calculates and displays travel expenses.')
... user_budget = int(input('Enter Budget: '))
... print()
... user_dest = (input('Enter your travel destination: '))
... print()
... user_gas = int(input('How much will you spend on gas? '))
... print()
... user_liv = int(input('Approximately, how much will you need for accomodation/hotel? '))
... print()
... user_food = int(input('Last, how much do you need for food? '))
... print('------------Travel Expenses------------')
... print('Location:', user_dest)
... print('Initial Budget:', user_budget, '\n')
... 
... print('Fuel:', user_gas)
... print('Accomodation:', user_liv)
... print('Food:', user_food, '\n')
... 
... user_exp = user_gas+user_liv+user_food
... user_bal = user_budget-user_exp
