# test passed
from model.customer import Customer
from data_access.customer_repository import CustomerRepository

customer_1=Customer(1,"mohammad","shafeie","09900660515")
customer_2=Customer(2,"sepideh","vahabali","09051272437")

customers=[customer_1,customer_2]

customer_3=Customer(3,"ali","ahmadi","09366453763")

repository=CustomerRepository()

repository.save_customers(customers)

repository.add_customer(customer_3)

result=repository.load_customers()

for customer in result:
    print(customer)
