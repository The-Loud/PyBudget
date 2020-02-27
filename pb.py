from prettytable import PrettyTable
from sqlalchemy.exc import SQLAlchemyError
import db_init as ts
from connection import Session, DB_ENG
import uuid


# Using the mariadb connection
ts.meta.create_all(DB_ENG['sql'])
session = Session()




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
    d = []
    done = 'n'
    while done != 'y':
        try:
            newid = uuid.uuid1().hex
            name, desc = input("What is the account name and description?: ")
            d.append(ts.Accounts(name=name, description=desc, account_ud=uuid.uuid1().hex))
            done = input('Would you like to add another? (y/n): ')
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
        finally:
            session.close()


try:
    for _val in add_account():
        session.add(_val)
    session.commit()
except SQLAlchemyError as e:
    print(e)
finally:
    session.close()
