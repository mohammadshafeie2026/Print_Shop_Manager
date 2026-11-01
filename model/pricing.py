from tools.validation import Validator
class Pricing:
    def __init__(self,printing_price,litho_price,cellophane_price_per_cm):
        self.printing_price=printing_price
        self.litho_price=litho_price
        self.cellophane_price_per_cm=cellophane_price_per_cm

    @property
    def printing_price(self):
        return self.__printing_price

    @printing_price.setter
    def printing_price(self, printing_price):
        Validator.printing_price_validator(printing_price)
        self.__printing_price=printing_price

    @property
    def litho_price(self):
        return self.__litho_price

    @litho_price.setter
    def litho_price(self, litho_price):
        Validator.litho_price_validator(litho_price)
        self.__litho_price=litho_price

    @property
    def cellophane_price_per_cm(self):
        return self.__cellophane_price_per_cm

    @cellophane_price_per_cm.setter
    def cellophane_price_per_cm(self, cellophane_price_per_cm):
        Validator.cellophane_price_per_cm_validator(cellophane_price_per_cm)
        self.__cellophane_price_per_cm=cellophane_price_per_cm


