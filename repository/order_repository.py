from alchemy.session import session
from models.customer_model import OrderModel


class OrderRepository:
    def __init__(self):
        self.__session = session
        self.__model = OrderModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, order_id):
        order = self.__session.get(self.__model, order_id)
        return order

    def add_item(self, order: OrderModel):
        self.__session.add(order)

    def update_item(self, order_id, new_order_date):
        order = self.__session.get(self.__model, order_id)
        order.new_order_date = new_order_date

    def remove_item_by_id(self, order_id):
        order = self.__session.get(self.__model, order_id)
        self.__session.delete(order)

if __name__ == "__main__":
    order_repo = OrderRepository()
    result = order_repo.get_all()
    for order in result:
        print(order)
        print(order.order_id)
