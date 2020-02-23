from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# psycopg2
postgres_engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')


# PyMySQL
sql_engine = create_engine('mysql+pymysql://user:password@yeet.local/pybudget')


DB_ENG = {'sql': sql_engine,
          'pst': postgres_engine}

Session = sessionmaker(bind=DB_ENG['sql'])
