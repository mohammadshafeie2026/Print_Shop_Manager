from data_access.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.repository=CustomerRepository()

    def add_customer(self,customer):
        self.repository.add_customer(customer)

    def get_all_customers(self):
        customers=self.repository.load_customers()
        return customers
