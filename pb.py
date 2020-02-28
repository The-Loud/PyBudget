from prettytable import PrettyTable
from sqlalchemy.exc import SQLAlchemyError
import db_init as ts
from connection import DB_ENG
import uuid
from sqlalchemy.orm import sessionmaker


# Using the mariadb connection
Session = sessionmaker(bind=DB_ENG['sql'])
session = Session()
ts.Base.metadata.create_all(DB_ENG['sql'])


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
    done = 'y'
    while done != 'n':
        try:
            name, desc = input("What is the account name and description?: ").split()
            d.append(ts.Accounts(name=name, description=desc, account_id=uuid.uuid1().hex))
            done = input('Would you like to add another? (y/n): ')
        except ValueError as e:
            print(e)
            print('\n')
            print("Please enter a valid name and account description")
            continue

        try:
            for _val in d:
                session.add(_val)
            session.commit()
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
        finally:
            session.close()


if __name__ == '__main__':
    add_account()
