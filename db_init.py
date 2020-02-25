from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from connection import DB_ENG, Session
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


meta = MetaData()
Base = declarative_base()


class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)
    reconciled = Column('reconciled', TINYINT)
    account_id = Column('account_id', INTEGER, ForeignKey('accounts.id'), nullable=False)
    description = Column('description', VARCHAR(length=1024))
    account_name = Column('description', VARCHAR(length=1024))
    amount = Column('amount', DECIMAL(precision=22, scale=2))

    def __repr__(self):
        return f"{self.id}, {self.created_at}, {self.updated_at},\
                 {self.deleted_at}, {self.reconciled},\
                 {self.account_id}, {self.description}, {self.amount}"


class Accounts(Base):
    __tablename__ = 'accounts'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)
    account_id = Column('account_id', INTEGER(unsigned=True))
    description = Column('description', VARCHAR(length=1024))
    name = Column('name', VARCHAR(length=250), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.created_at}, {self.updated_at},\
                 {self.deleted_at}, {self.account_id},\
                 {self.description}, {self.name}"


class Assets(Base):
    __tablename__ = 'assets'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = Column('created_at', TIMESTAMP, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP)
    deleted_at = Column('deleted_at', TIMESTAMP)
    account_id = Column('account_id', INTEGER(unsigned=True))
    description = Column('description', VARCHAR(length=1024))
    name = Column('name', VARCHAR(length=250), nullable=False)
    amount = Column('amount', DECIMAL(precision=22, scale=2))

    def __repr__(self):
        return f"{self.id}, {self.created_at}, {self.updated_at},\
                 {self.deleted_at}, {self.account_id},\
                 {self.description}, {self.name}, {self.amount}"

    def go(self, session):
        session.query(Assets).update({"q": 18})
