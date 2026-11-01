import os
import pickle
class OrderRepository:
    def __init__(self):
        self.file_path=os.path.join("data","orders.pkl")

    def load_orders(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path,"rb") as file:
            orders=pickle.load(file)
            return orders

    def save_orders(self,orders):
        with open(self.file_path,"wb") as file:
            pickle.dump(orders,file)

    def add_order(self,order):
        orders=self.load_orders()
        orders.append(order)
        self.save_orders(orders)



