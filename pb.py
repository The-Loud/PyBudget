from prettytable import PrettyTable
from sqlalchemy.exc import SQLAlchemyError
import db_init as ts
from connection import Session, DB_ENG

# Using the mariadb connection
ts.meta.create_all(DB_ENG['sql'])
session = Session()

account = ts.Accounts(name="savings", description="test description")


# Let's get some user input now.
def menu():
    show = PrettyTable(["Menu"])
    show.add_row(["Ones"])

    print(menu)


def welcome():
    print('Welcome to PyBudget!\n')
    print('Here\'s a list of available commands:\n')
    print('1. View balances\n\
           2. Add a transaction\n\
           3. View transactions\n\
           4. Create an account')
    return int(input("What would you like to do?: "))


def add_account():
    d = {}
    done = 'n'
    while done != 'y':
        name, desc = input("What is the account name and description?: ")
        d[name] = desc
        done = input('Would you like to add another? (y/n): ')

'''
try:
    for _key, _val in d.items():
        row = ts.Accounts(name=_key, description=_val)
        session.add(row)
    session.commit()
except SQLAlchemyError as e:
    print(e)
finally:
    session.close()
'''
