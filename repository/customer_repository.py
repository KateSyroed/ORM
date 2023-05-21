from models.customer_model import CustomerModel
from alchemy.session import session
from models.order_model import OrderModel



class CustomerRepository:
    def __init__(self):
        self.__session = session
        self.__model = CustomerModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, customer_id):
        customer = self.__session.get(self.__model, customer_id)
        return customer

    def add_item(self, customer: CustomerModel):
        self.__session.add(customer)

    def remove_item_by_id(self, customer_id):
        customer = self.__session.get(self.__model, customer_id)
        self.__session.delete(customer)

if __name__ == "__main__":
    customer_repo = CustomerRepository()
    result = customer_repo.get_all()
    for customer in result:
        print(customer)
        print(customer.customer_id)
