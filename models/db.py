from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

from config import Config

Base = declarative_base()

engine = create_engine(Config.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

#Base contains a Metadata object where newly created Table objects are collected
# metadata = MetaData(engine)
# metadata.reflect(bind=engine)

db = SQLAlchemy()
