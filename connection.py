from sqlalchemy import create_engine

# psycopg2
postgres_engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')


# PyMySQL
sql_engine = create_engine('mysql+pymysql://user:somepass@yeet.local/pybudget')


DB_ENG = {'sql': sql_engine,
          'pst': postgres_engine}
