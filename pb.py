from connection import Session, DB_ENG
from db_init import *
from sqlalchemy.exc import SQLAlchemyError

meta.create_all(DB_ENG['sql'])
session = Session()

account = Accounts(name="savings", description="test description")
d = {"retirement": "an account for retirement"}
# session.add(account)
# session.commit()
# session.close()

try:
    for _key, _val in d.items():
        row = Accounts(name=_key, description=_val)
        session.add(row)
    session.commit()
except SQLAlchemyError as e:
    print(e)
finally:
    session.close()
'''
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
'''
