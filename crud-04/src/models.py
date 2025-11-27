from database import Base
from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class StoreModel(Base):
    __tablename__ = "store"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    address = Column(String,nullable=False)
    zipcode = Column(Integer, nullable=False)
    city = Column(String,nullable=False)
    state = Column(String,nullable=False)
    createdAt = Column(DateTime(timezone=True),server_default=func.now())
    updatedAt = Column(DateTime(timezone=True),onupdate=func.now())

class EmployeeModel(Base):
    __tablename__ = "employee"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    birthdate = Column(Date,nullable=False)
    position = Column(String,nullable=False)
    startDate = Column(Date,nullable=False)
    storeId = Column(Integer,ForeignKey("store.id"))
    createdAt = Column(DateTime(timezone=True),server_default=func.now())
    updatedAt = Column(DateTime(timezone=True),onupdate=func.now())
