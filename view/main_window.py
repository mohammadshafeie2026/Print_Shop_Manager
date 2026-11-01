import tkinter as tk
from tkinter import ttk

from view.customer_window import CustomerWindow
from view.order_window import OrderWindow
from view.pricing_window import PricingWindow


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Print Shop Manager")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        title = ttk.Label(
            root,
            text="Print Shop Management System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=35)

        ttk.Button(
            root, text="Customer Management",
            command=self.open_customer_window, width=30
        ).pack(pady=10)

        ttk.Button(
            root, text="Order Management",
            command=self.open_order_window, width=30
        ).pack(pady=10)

        ttk.Button(
            root, text="Order Pricing",
            command=self.open_pricing_window, width=30
        ).pack(pady=10)

        ttk.Button(
            root, text="Exit",
            command=self.root.destroy, width=30
        ).pack(pady=25)

    def open_customer_window(self):
        CustomerWindow(self.root)

    def open_order_window(self):
        OrderWindow(self.root)

    def open_pricing_window(self):
        PricingWindow(self.root)
