from model.pricing import Pricing
from model.order import Order
from model.customer import Customer

from business_logic.pricing_price import calculate_order_price

from datetime import date

# test passed
# customer=Customer(1,"mohammad","shafeie","09120660515")
#
# order_1=Order(140501,
#               customer,
#               date(2026,10,30),
#               50,
#               30,
#               6000,
#               4
#               )
# pricing=Pricing(25_000_000,4_500_000,10)
#
# result=calculate_order_price(order_1,pricing)
#
# print(result)
# ...............................................................

#test passed

# customer=Customer(1,"mohammad","shafeie","09120660515")
#
# order_1=Order(140501,
#               customer,
#               date(2026,10,30),
#               50,
#               30,
#               5001,
#               4
#               )
# pricing=Pricing(25_000_000,4_500_000,10)
#
# result=calculate_order_price(order_1,pricing)
#
# print(result)

# ...............................................................................

customer=Customer(1,"mohammad","shafeie","09120660515")

order_1=Order(140501,
              customer,
              date(2026,10,30),
              50,
              30,
              5000,
              4
              )
pricing=Pricing(25_000_000,4_500_000,10)

result=calculate_order_price(order_1,pricing)

print(result)

