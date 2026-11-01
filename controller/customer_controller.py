from business_logic.customer_service import CustomerService

class CustomerController:
    def __init__(self):
        self.service=CustomerService()

    def add_customer(self,customer):
        return  self.service.add_customer(customer)

    def get_all_customers(self):
        return self.service.get_all_customers()
