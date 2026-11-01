from model.customer import Customer
from model.order import Order
from datetime import date,timedelta
from tools.validation import Validator

customer_1=Customer(1,"mohammad","shafeie","09900660515")

delivery=date.today()+timedelta(days=3)

order_1=Order(40501,customer_1,delivery,100,70,5000,4)

print(order_1)
print(order_1.order_id)
print(order_1.customer)
print(order_1.order_date)
print(order_1.delivery_date)
print(order_1.to_tuple())
