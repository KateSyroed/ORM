from models.order_model import OrderModel
from alchemy.session import session


class OrderRepository:
    def __init__(self):
        self.__session = session
        self.__model = OrderModel

    def get_all(self):
        return self.__session.query(self.__model).all()

if __name__ == "__main__":
    order_repo = OrderRepository()
    result = order_repo.get_all()
    for u in result:
        print(u)

