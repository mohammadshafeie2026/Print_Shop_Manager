from business_logic.order_service import OrderService

class OrderController:
    def __init__(self):
        self.service=OrderService()

    def add_order(self,order):
        return self.service.add_order(order)

    def get_all_orders(self):
        return self.service.get_all_orders()
