from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://doadmin:AVNS_zOQUWFt21cxvigclv9x@db-mysql-nyc3-80012-do-user-15899616-0.c.db.ondigitalocean.com:25060/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'ssl_ca': '/path/to/ca.pem'})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()