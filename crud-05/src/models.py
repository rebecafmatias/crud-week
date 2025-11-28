from sqlalchemy import Column, String, Integer, Float, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class SalesModel(Base):
    __tablename__ = "sales"

    order_id = Column(Integer,nullable=False)
    customer_name = Column(String,nullable=False)
    product = Column(String,nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    sale_date = Column(Date,nullable=False)
    createdAt = Column(DateTime(timezone=True),func.)