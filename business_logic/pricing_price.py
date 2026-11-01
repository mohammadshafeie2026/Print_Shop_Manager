def calculate_printing_cost(sheets):
    if sheets % 5000==0:
        n=int(sheets / 5000)
    else:
        n=int(sheets / 5000)+1
    price=int(n*25_000_000)
    return price

def calculate_litho_cost(color_count,price_per_plate):
    price=color_count * price_per_plate
    return price

def calculate_cellophane_cost(length,width,sheet_count,price_per_cm):
    return length*width*sheet_count*price_per_cm

def calculate_total_price(print_cost,litho_cost,cellophane_cost):
    return print_cost + litho_cost + cellophane_cost

def calculate_order_price(order,pricing):
    print_cost=calculate_printing_cost(order.sheet_count)
    litho_cost=calculate_litho_cost(order.color_count,pricing.litho_price)
    cellophane_cost=calculate_cellophane_cost(order.length,order.width,order.sheet_count,pricing.cellophane_price_per_cm)
    total_price=calculate_total_price(print_cost,litho_cost,cellophane_cost)

    return f"Total Price is:{total_price} Toman"


