from business_logic.pricing_price import calculate_order_price

class PricingController:
    def calculate_order_price(self, order, pricing):
        return calculate_order_price(order, pricing)

