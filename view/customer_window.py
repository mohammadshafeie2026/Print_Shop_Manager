import tkinter as tk
from tkinter import ttk, messagebox

from model.customer import Customer
from controller.customer_controller import CustomerController

class CustomerWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Customer Management")
        self.window.geometry("750x500")

        self.controller = CustomerController()

        form = ttk.LabelFrame(self.window, text="New Customer", padding=10)
        form.pack(fill="x", padx=12, pady=10)

        self.entries = {}
        fields = [
            ("Customer ID", "customer_id"),
            ("Name", "name"),
            ("Family", "family"),
            ("Phone", "phone"),
        ]

        for row, (label, key) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=row, column=0, padx=6, pady=5, sticky="w")
            entry = ttk.Entry(form, width=30)
            entry.grid(row=row, column=1, padx=6, pady=5)
            self.entries[key] = entry

        ttk.Button(form, text="Add Customer", command=self.add_customer).grid(
            row=4, column=0, columnspan=2, pady=10
        )

        columns = ("customer_id", "name", "family", "phone")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        headings = {
            "customer_id": "ID",
            "name": "Name",
            "family": "Family",
            "phone": "Phone",
        }
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=150)
        self.tree.pack(fill="both", expand=True, padx=12, pady=10)

        self.refresh_customers()

    def add_customer(self):
        try:
            customer_id = self.entries["customer_id"].get()

            if not customer_id.strip():
                raise ValueError("Customer ID cannot be empty!")
            customer = Customer(
                int(int(self.entries["customer_id"].get())),
                self.entries["name"].get(),
                self.entries["family"].get(),
                self.entries["phone"].get()
            )
            self.controller.add_customer(customer)
            messagebox.showinfo("Success", "Customer added successfully.")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.refresh_customers()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def refresh_customers(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            customers = self.controller.get_all_customers()
            for customer in customers:
                self.tree.insert("", tk.END, values=customer.to_tuple())
        except Exception as error:
            messagebox.showerror("Error", str(error))
