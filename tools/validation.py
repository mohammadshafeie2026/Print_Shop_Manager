import re
from datetime import date


class Validator:
    @staticmethod
    def customer_id_validator(customer_id):
        if isinstance(customer_id, int) and customer_id > 0:
            return True
        else:
            raise ValueError("Invalid ID")
    @staticmethod
    def name_validator(name):
        if not isinstance(name, str):
            raise ValueError("name must be a string")

        if not re.match(r"^[a-zA-Z\s]{2,30}$", name):
            raise ValueError("Invalid Name")

        return True

    @staticmethod
    def family_validator(family):
        if not isinstance(family, str):
            raise ValueError("family must be a string")

        if not re.match(r"^[a-zA-Z\s]{2,40}$", family):
            raise ValueError("Invalid Family")

        return True

    @staticmethod
    def phone_validator(phone):
        if not isinstance(phone, str):
            raise ValueError("phone number must be a string")

        if not re.match(r"^09[0-9]{9}$", phone):
            raise ValueError("Invalid Phone Number.")

        return True

    @staticmethod
    def order_id_validator(order_id):
        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError("invalid order ID")

        return True

    @staticmethod
    def customer_validator(customer):
        from model.customer import Customer
        if isinstance(customer, Customer):
            return True
        else:
            raise ValueError("invalid customer")


    @staticmethod
    def delivery_date_validator(delivery_date):
        if not isinstance(delivery_date, date):
            raise ValueError("Invalid date")

        if delivery_date < date.today():
            raise ValueError("delivery date can not be in the past")

        return True

    @staticmethod
    def length_validator(length):
        if not isinstance(length,(int,float)):
            raise ValueError("length must be a number")
        if length<=0:
            raise ValueError("length must be positive")

        return True

    @staticmethod
    def width_validator(width):
        if not isinstance(width, (int, float)):
            raise ValueError("width must be a number")
        if width <= 0:
            raise ValueError("width must be positive")

        return True

    @staticmethod
    def sheet_count_validator(sheet_count):
        if not isinstance(sheet_count,int):
            raise ValueError("sheet count must be a number")
        if sheet_count <= 0:
            raise ValueError("sheet count must be positive")

        return True

    @staticmethod
    def color_count_validator(color_count):
        if not isinstance(color_count, int):
            raise ValueError("color count must be a number")
        if  not 0<color_count<=6 :
            raise ValueError("color count must between 1 until 6 color")

        return True

    @staticmethod
    def printing_price_validator(printing_price):
        if not isinstance(printing_price,(int,float)) or printing_price<=0:
            raise ValueError("Invalid price")
        return True

    @staticmethod
    def litho_price_validator(litho_price):
        if not isinstance(litho_price, (int, float)) or litho_price <= 0:
            raise ValueError("Invalid price")
        return True

    @staticmethod
    def cellophane_price_per_cm_validator(cellophane_price_per_cm):
        if not isinstance(cellophane_price_per_cm, (int, float)) or cellophane_price_per_cm <= 0:
            raise ValueError("Invalid price")
        return True





