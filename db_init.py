from connection import DB_ENG
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


meta = MetaData()

# Transaction table
transactions = Table('transactions', meta,
                     Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
                     Column('created_at', TIMESTAMP, nullable=False),
                     Column('updated_at', TIMESTAMP),
                     Column('deleted_at', TIMESTAMP),
                     Column('reconciled', TINYINT),
                     Column('account_id', INTEGER, ForeignKey('accounts.id'), nullable=False),
                     Column('description', VARCHAR(length=1024)),
                     Column('amount', DECIMAL(precision=22, scale=2)))

accounts = Table('accounts', meta,
                 Column('id', Integer, primary_key=True, autoincrement=True, nullable=False),
                 Column('created_at', TIMESTAMP, nullable=False),
                 Column('updated_at', TIMESTAMP),
                 Column('deleted_at', TIMESTAMP),
                 Column('account_id', INTEGER(unsigned=True)),
                 Column('description', VARCHAR(length=1024)),
                 Column('name', VARCHAR(length=250), nullable=False))

meta.create_all(DB_ENG['sql'])
