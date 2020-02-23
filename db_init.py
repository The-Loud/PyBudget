from connection import DB_ENG
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, declarative_base
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


meta = MetaData()
Base = declarative_base

# Transaction table
# Refactor these to have classes instead.

class Transactions(Base):
    __tablename__ = 'transactions'

    p_id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)
    reconciled = Column('reconciled', TINYINT)
    account_id = Column('account_id', INTEGER, ForeignKey('accounts.id'), nullable=False)
    description = Column('description', VARCHAR(length=1024))
    amount = Column('amount', DECIMAL(precision=22, scale=2))

    def __repr__(self):
        return f"{self.p_id}, {created_at}, {updated_at},\
                 {deleted_at}, {reconciled}, {account_id}, {description}, {amount}"


class Accounts(Base):
    __tablename__ = 'accounts'

    p_id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    created_at = Column('created_at', TIMESTAMP, nullable=False),
    updated_at = Column('updated_at', TIMESTAMP),
    deleted_at = Column('deleted_at', TIMESTAMP),
    account_id = Column('account_id', INTEGER(unsigned=True)),
    description = Column('description', VARCHAR(length=1024)),
    name = Column('name', VARCHAR(length=250), nullable=False))


    def __repr__(self):
        return f"{self.p_id}, {created_at}, {updated_at},\
                 {deleted_at}, {account_id}, {description}, {name}"


'''
accounts = Table('accounts', meta,
                 Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
                 Column('created_at', TIMESTAMP, nullable=False),
                 Column('updated_at', TIMESTAMP),
                 Column('deleted_at', TIMESTAMP),
                 Column('account_id', INTEGER(unsigned=True)),
                 Column('description', VARCHAR(length=1024)),
                 Column('name', VARCHAR(length=250), nullable=False))
'''
meta.create_all(DB_ENG['sql'])
