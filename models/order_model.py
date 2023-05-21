from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, INTEGER, ForeignKey, DATE, VARCHAR


Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = "customers"
    customer_id = Column(INTEGER, primary_key=True)
    customer_name = Column(VARCHAR(50))
    orders = relationship("OrderModel", back_populates="customer")

    def __str__(self):
        return f"id = {self.customer_id}, title = {self.customer_name}"

    class OrderModel(Base):
        __tablename__ = 'orders'
        order_id = Column(INTEGER, primary_key=True)
        customer_id = Column(INTEGER, ForeignKey('customers.customer_id'))

    def __int__(self):
        return f"id = {self.order_id}, order_date = {self.order_date},  customer = {self.customer_id}"

