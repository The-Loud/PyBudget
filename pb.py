from connection import Session, DB_ENG
from db_init import *

meta.create_all(DB_ENG['sql'])
session = Session()

account = Accounts(name="savings", description="test description")

session.add(account)
session.commit()
session.close()
'''
#@contextmanager
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
