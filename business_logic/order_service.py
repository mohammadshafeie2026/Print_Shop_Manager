from data_access.order_repository import OrderRepository

class OrderService:
    def __init__(self):
        self.repository=OrderRepository()

    def add_order(self,order):
        self.repository.add_order(order)

    def get_all_orders(self):
        orders=self.repository.load_orders()
        return orders