from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.sql import func
from database import Base

class EmployeesModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    gender = Column(String,nullable=False)
    birthdate = Column(DateTime,nullable=False)
    address =   Column(String, nullable=False)
    start_date = Column(DateTime,nullable=False)
    position = Column(String,nullable=False)
    monthly_salary = Column(Float, nullable=False)

