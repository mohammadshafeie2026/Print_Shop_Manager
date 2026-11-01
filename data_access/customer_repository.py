import os
import pickle

class CustomerRepository:
    def __init__(self):
        self.file_path = os.path.join("data", "customers.pkl")

    def load_customers(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "rb") as file:
            customers = pickle.load(file)

        return customers

    def save_customers(self, customers):
        with open(self.file_path, "wb") as file:
            pickle.dump(customers, file)

    def add_customer(self,customer):
        customers=self.load_customers()
        customers.append(customer)
        self.save_customers(customers)
