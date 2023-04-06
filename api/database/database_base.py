from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Settings

settings = Settings()

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.db_database
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)