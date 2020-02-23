from connection import DB_ENG, Session
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

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)
    reconciled = Column('reconciled', TINYINT)
    account_id = Column('account_id', INTEGER, ForeignKey('accounts.id'), nullable=False)
    description = Column('description', VARCHAR(length=1024))
    amount = Column('amount', DECIMAL(precision=22, scale=2))


    def __init(self, amount, desc, account):
        self.description = desc
        self.amount = amount
        self.account = account


    def __repr__(self):
        return f"{self.id}, {created_at}, {updated_at},\
                 {deleted_at}, {reconciled}, {account_id}, {description}, {amount}"


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    created_at = Column('created_at', TIMESTAMP, nullable=False),
    updated_at = Column('updated_at', TIMESTAMP),
    deleted_at = Column('deleted_at', TIMESTAMP),
    account_id = Column('account_id', INTEGER(unsigned=True)),
    description = Column('description', VARCHAR(length=1024)),
    name = Column('name', VARCHAR(length=250), nullable=False))


    def __init__(self, name, desc):
        self.name = name
        self.description = desc


    def __repr__(self):
        return f"{self.id}, {created_at}, {updated_at},\
                 {deleted_at}, {account_id}, {description}, {name}"


class Assets(Base):
    __tablename__ = 'accounts'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
    created_at = Column('created_at', TIMESTAMP, nullable=False),
    updated_at = Column('updated_at', TIMESTAMP),
    deleted_at = Column('deleted_at', TIMESTAMP),
    account_id = Column('account_id', INTEGER(unsigned=True)),
    description = Column('description', VARCHAR(length=1024)),
    name = Column('name', VARCHAR(length=250), nullable=False))
    amount = Column('amount', DECIMAL(precision=22, scale=2)


    def __init__(self, name, desc, amount):
        self.name = name
        self.description = desc
        self.amount = amount


    def __repr__(self):
        return f"{self.id}, {created_at}, {updated_at},\
                 {deleted_at}, {account_id}, {description}, {name}, {amount}"


meta.create_all(DB_ENG['sql'])
session = Session()
