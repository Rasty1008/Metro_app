from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Schedule(Base):
    __tablename__ = "Schedule"

    id = Column(Integer, primary_key=True)
    stations = Column(String)
    rayymbek_momyshuly = Column(String)
    momyshuly_rayymbek = Column(String)
