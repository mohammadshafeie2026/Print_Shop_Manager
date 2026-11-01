from datetime import date
from tools.validation import Validator

class Order:
    def __init__(self, order_id, customer, delivery_date,length,width,sheet_count,color_count):
        self.order_id = order_id
        self.customer = customer
        self.order_date = date.today()
        self.delivery_date = delivery_date
        self.length=length
        self.width=width
        self.sheet_count=sheet_count
        self.color_count=color_count

    @property
    def order_id(self):
        return self.__order_id

    @order_id.setter
    def order_id(self, order_id):
        Validator.order_id_validator(order_id)
        self.__order_id=order_id

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        Validator.customer_validator(customer)
        self.__customer=customer

    @property
    def delivery_date(self):
        return self.__delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        Validator.delivery_date_validator(delivery_date)
        self.__delivery_date=delivery_date

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        Validator.length_validator(length)
        self.__length=length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        Validator.width_validator(width)
        self.__width=width

    @property
    def sheet_count(self):
        return self.__sheet_count

    @sheet_count.setter
    def sheet_count(self, sheet_count):
        Validator.sheet_count_validator(sheet_count)
        self.__sheet_count=sheet_count

    @property
    def color_count(self):
        return self.__color_count

    @color_count.setter
    def color_count(self, color_count):
        Validator.color_count_validator(color_count)
        self.__color_count=color_count


    def __str__(self):
        return f"Order ID: {self.order_id} | Customer: {self.customer.name} {self.customer.family}"

    def to_tuple(self):
        return (self.order_id,
                self.customer.name,
                self.customer.family,
                self.order_date,
                self.delivery_date,
                self.length,
                self.width,
                self.sheet_count,
                self.color_count
        )


