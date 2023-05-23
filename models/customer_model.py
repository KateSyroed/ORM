from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, INTEGER, ForeignKey, DATE, String

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = "customers"
    customer_id = Column(INTEGER, primary_key=True, name="customerid")
    customer_name = Column(String, name="customername")  # Updated column name
    orders = relationship("OrderModel", back_populates="customer")

    def __str__(self):
        return f"id = {self.customer_id}, title = {self.customer_name}"

class OrderModel(Base):
    __tablename__ = 'orders'
    order_id = Column(INTEGER, primary_key=True, name="orderid")  # Updated column name
    customer_id = Column(INTEGER, ForeignKey('customers.customerid'))
    customer = relationship("CustomerModel", back_populates="orders")

    def __int__(self):
        return f"id = {self.order_id}, order_date = {self.order_date},  customer = {self.customer_id}"
