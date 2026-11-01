# test passed
from model.order import Order
from data_access.order_repository import OrderRepository
from model.customer import Customer
from datetime import date


customer_1=Customer(1,"mohammad","shafeie","09900660515")
customer_2=Customer(2,"sepideh","vahabali","09051272437")
customer_3=Customer(3,"reza","rajabi","09123726503")

delivery=date.today()

order_1=Order(1,customer_1,delivery,100,50,2000,4)
order_2=Order(2,customer_2,delivery,80,70,3000,5)

orders=[order_1,order_2]

order_3=Order(3,customer_2,delivery,80,70,3000,5)

repository=OrderRepository()

repository.save_orders(orders)

repository.add_order(order_3)

a=repository.load_orders()

for order in a:
    print(order)
