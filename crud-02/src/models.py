from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import func
from database import Base

class BrazilCitiesModel(Base):
    __tablename__ = "brazil_cities"

    id = Column(Integer,primary_key=True)
    city = Column(String,nullable=False)
    state = Column(String,nullable=False)
    area_code = Column(Integer,nullable=True)