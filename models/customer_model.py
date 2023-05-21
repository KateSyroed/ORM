from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class CustomerModel(Base):
    __tablename__ = 'customers'
    customer_id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50))
    orders = relationship("OrderModel", backref="customer")

    def __str__(self):
        return f"id = {self.customer_id}, title = {self.customer_name}"