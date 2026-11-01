# test passed
from model.customer import Customer
from tools.validation import Validator
from model.order import Order
from datetime import timedelta,date

from tools.validation import Validator
def test_valid(test_name,validator,value):
    try:
        validator(value)
    except ValueError:
        print(f"{test_name}: Failed")
    else:
        print(f"{test_name}:Passed")

def test_invalid(test_name,validator,value):
    try:
        validator(value)
    except ValueError:
        print(f"{test_name}:Passed")
    else:
        print(f"{test_name}:Failed")


customer = Customer(1, "Ali", "Alipour", "09123456789")

# Order ID
test_valid("Order ID Valid", Validator.order_id_validator, 140501)
test_invalid("Order ID Invalid", Validator.order_id_validator, 0)

# Customer
test_valid("Customer Valid", Validator.customer_validator, customer)
test_invalid("Customer Invalid", Validator.customer_validator, "Ali")

# Delivery Date
test_valid(
    "Delivery Date Valid",
    Validator.delivery_date_validator,
    date.today() + timedelta(days=3)
)

test_invalid(
    "Delivery Date Invalid",
    Validator.delivery_date_validator,
    date.today() - timedelta(days=1)
)

# Length
test_valid("Length Valid", Validator.length_validator, 70)
test_invalid("Length Invalid", Validator.length_validator, 0)

# Width
test_valid("Width Valid", Validator.width_validator, 100)
test_invalid("Width Invalid", Validator.width_validator, -10)

# Sheet Count
test_valid("Sheet Count Valid", Validator.sheet_count_validator, 5000)
test_invalid("Sheet Count Invalid", Validator.sheet_count_validator, 0)

# Color Count
test_valid("Color Count Valid", Validator.color_count_validator, 4)
test_invalid("Color Count Invalid", Validator.color_count_validator, 7)
