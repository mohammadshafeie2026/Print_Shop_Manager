import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from model.order import Order
from controller.order_controller import OrderController
from controller.customer_controller import CustomerController


class OrderWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Order Management")
        self.window.geometry("1000x600")

        self.order_controller = OrderController()
        self.customer_controller = CustomerController()
        self.customers = []

        form = ttk.LabelFrame(self.window, text="New Order", padding=10)
        form.pack(fill="x", padx=12, pady=10)

        self.entries = {}
        fields = [
            ("Order ID", "order_id"),
            ("Delivery Date (YYYY-MM-DD)", "delivery_date"),
            ("Length (cm)", "length"),
            ("Width (cm)", "width"),
            ("Sheet Count", "sheet_count"),
        ]

        for row, (label, key) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=row, column=0, padx=6, pady=4, sticky="w")
            entry = ttk.Entry(form, width=25)
            entry.grid(row=row, column=1, padx=6, pady=4)
            self.entries[key] = entry

        ttk.Label(form, text="Customer").grid(row=0, column=2, padx=6, pady=4, sticky="w")
        self.customer_box = ttk.Combobox(form, state="readonly", width=35)
        self.customer_box.grid(row=0, column=3, padx=6, pady=4)

        ttk.Label(form, text="Color Count").grid(row=1, column=2, padx=6, pady=4, sticky="w")
        self.color_box = ttk.Combobox(
            form, state="readonly", values=[1, 2, 3, 4, 5, 6], width=33
        )
        self.color_box.grid(row=1, column=3, padx=6, pady=4)

        ttk.Button(form, text="Add Order", command=self.add_order).grid(
            row=5, column=0, columnspan=4, pady=10
        )

        columns = (
            "order_id", "customer", "order_date", "delivery_date",
            "length", "width", "sheet_count", "color_count"
        )
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        titles = (
            "Order ID", "Customer", "Order Date", "Delivery Date",
            "Length", "Width", "Sheets", "Colors"
        )
        for column, title in zip(columns, titles):
            self.tree.heading(column, text=title)
            self.tree.column(column, width=115)
        self.tree.pack(fill="both", expand=True, padx=12, pady=10)

        self.refresh_customers()
        self.refresh_orders()

    def refresh_customers(self):
        try:
            self.customers = self.customer_controller.get_all_customers()
            self.customer_box["values"] = [
                f"{customer.customer_id} - {customer.name} {customer.family}"
                for customer in self.customers
            ]
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def add_order(self):
        try:
            order_id = self.entries["order_id"].get()

            if not order_id.strip():
                raise ValueError("Order ID cannot be empty!")
            selected_index = self.customer_box.current()
            if selected_index < 0:
                raise ValueError("Please select a customer.")

            customer = self.customers[selected_index]
            delivery_date = date.fromisoformat(self.entries["delivery_date"].get())

            order = Order(
                int(order_id),
                customer,
                delivery_date,
                float(self.entries["length"].get()),
                float(self.entries["width"].get()),
                int(self.entries["sheet_count"].get()),
                int(self.color_box.get())
            )

            self.order_controller.add_order(order)
            messagebox.showinfo("Success", "Order added successfully.")

            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.color_box.set("")
            self.customer_box.set("")
            self.refresh_orders()

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def refresh_orders(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            orders = self.order_controller.get_all_orders()
            for order in orders:
                self.tree.insert(
                    "", tk.END,
                    values=(
                        order.order_id,
                        f"{order.customer.name} {order.customer.family}",
                        order.order_date,
                        order.delivery_date,
                        order.length,
                        order.width,
                        order.sheet_count,
                        order.color_count
                    )
                )
        except Exception as error:
            messagebox.showerror("Error", str(error))
