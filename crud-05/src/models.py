from sqlalchemy import Column, String, Integer, Float, Date, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class SalesModel(Base):
    __tablename__ = "sales"

    id = Column(Integer,primary_key=True)
    order_id = Column(Integer, nullable=False,unique=True)
    customer_name = Column(String,nullable=False)
    product = Column(String,nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    sale_date = Column(Date,nullable=False)
    total_price = Column(Float,nullable=False)
    updatedAt = Column(DateTime(timezone=True),onupdate=func.now())
    createdAt = Column(DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return f"Sale(id={self.id},customer='{self.customer_name}',product='{self.product}')"
    
class OrderHistoryModel(Base):
    __tablename__ = "order_history"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("sales.order_id"))
    status = Column(String,nullable=False)
    statusDateTime = Column(DateTime(timezone=True),nullable=False) 
    createdAt = Column(DateTime(timezone=True),server_default=func.now())