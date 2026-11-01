import tkinter as tk
from tkinter import ttk, messagebox

from model.pricing import Pricing
from controller.order_controller import OrderController
from controller.pricing_controller import PricingController


class PricingWindow:
    # The current calculate_printing_cost function uses a fixed rate:
    # each 5000-sheet block costs 25,000,000 toman.
    PRINTING_PRICE_PER_5000 = 25_000_000

    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Order Pricing")
        self.window.geometry("750x500")

        self.order_controller = OrderController()
        self.pricing_controller = PricingController()
        self.orders = []

        form = ttk.LabelFrame(self.window, text="Calculate Order Price", padding=12)
        form.pack(fill="x", padx=12, pady=12)

        ttk.Label(form, text="Select Order").grid(row=0, column=0, padx=6, pady=8, sticky="w")
        self.order_box = ttk.Combobox(form, state="readonly", width=45)
        self.order_box.grid(row=0, column=1, padx=6, pady=8)

        ttk.Label(form, text="Lithography Price (per color)").grid(
            row=1, column=0, padx=6, pady=8, sticky="w"
        )
        self.litho_entry = ttk.Entry(form, width=48)
        self.litho_entry.grid(row=1, column=1, padx=6, pady=8)

        ttk.Label(form, text="Cellophane Price (per cm² per sheet)").grid(
            row=2, column=0, padx=6, pady=8, sticky="w"
        )
        self.cellophane_entry = ttk.Entry(form, width=48)
        self.cellophane_entry.grid(row=2, column=1, padx=6, pady=8)

        ttk.Label(
            form,
            text="Printing: 25,000,000 toman per 5,000 sheets (current calculation rule)"
        ).grid(row=3, column=0, columnspan=2, padx=6, pady=8)

        ttk.Button(form, text="Calculate", command=self.calculate_price).grid(
            row=4, column=0, columnspan=2, pady=12
        )

        self.result_label = ttk.Label(
            self.window, text="", font=("Arial", 14, "bold")
        )
        self.result_label.pack(pady=25)

        self.refresh_orders()

    def refresh_orders(self):
        try:
            self.orders = self.order_controller.get_all_orders()
            self.order_box["values"] = [
                f"{order.order_id} - {order.customer.name} {order.customer.family}"
                for order in self.orders
            ]
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def calculate_price(self):
        try:
            selected_index = self.order_box.current()
            if selected_index < 0:
                raise ValueError("Please select an order.")

            order = self.orders[selected_index]
            litho_text = self.litho_entry.get().strip()
            cellophane_text = self.cellophane_entry.get().strip()
            print("Litho:", repr(litho_text))
            print("Cellophane:", repr(cellophane_text))

            if not litho_text:
                raise ValueError("Lithography price cannot be empty!")

            if not cellophane_text:
                raise ValueError("Cellophane price cannot be empty!")

            litho_price = float(litho_text)
            cellophane_price = float(cellophane_text)

            pricing = Pricing(
                self.PRINTING_PRICE_PER_5000,
                litho_price,
                cellophane_price
            )

            result = self.pricing_controller.calculate_order_price(order, pricing)
            self.result_label.config(text=result)

        except Exception as error:
            import traceback
            traceback.print_exc()
            messagebox.showerror("Error", str(error))
