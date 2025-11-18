from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from databse import Base

class DogsBreedModel(Base):
    __tablename__ = "dogs_breed"

    id = Column(Integer,primary_key=True)
    breed_name = Column(String,nullable=False)
    origin_country = Column(String,nullable=True)
    colors = Column(String,nullable=True)
    description = Column(String,nullable=True)
    avg_life_range = Column(Float,nullable=True)
    avg_weight = Column(Float,nullable=True)
    createdAt = Column(DateTime(timezone=True),server_default=func.now())
    updatedAt = Column(DateTime(timezone=True),onupdate=func.now())
