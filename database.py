
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Ananya@2702")
host = "localhost"
port = "3306"
database_name = "products_db"

DATABASE_URL = (
    f"mysql+pymysql://{username}:{password}"
    f"@{host}:{port}/{database_name}"
)

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
