import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# Customer Data
# -----------------------------

customers = [
    ("C001", "Ravi", "Hyderabad", "Telangana"),
    ("C002", "Anjali", "Vijayawada", "Andhra Pradesh"),
    ("C003", "Kiran", "Chennai", "Tamil Nadu"),
    ("C004", "Priya", "Bengaluru", "Karnataka"),
    ("C005", "Arjun", "Mumbai", "Maharashtra"),
    ("C006", "Sneha", "Pune", "Maharashtra"),
    ("C007", "Rahul", "Delhi", "Delhi"),
    ("C008", "Meena", "Visakhapatnam", "Andhra Pradesh"),
    ("C009", "Vikram", "Kochi", "Kerala"),
    ("C010", "Divya", "Warangal", "Telangana")
]

# -----------------------------
# Product Data
# -----------------------------

products = [
    ("P001", "Laptop", "Electronics", 55000),
    ("P002", "Mouse", "Electronics", 800),
    ("P003", "Keyboard", "Electronics", 1500),
    ("P004", "Monitor", "Electronics", 12000),
    ("P005", "Headphones", "Electronics", 2500),
    ("P006", "Office Chair", "Furniture", 7500),
    ("P007", "Desk", "Furniture", 10000),
    ("P008", "Notebook", "Stationery", 120),
    ("P009", "Pen Set", "Stationery", 250),
    ("P010", "Backpack", "Accessories", 1800)
]

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

order_statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Cancelled",
    "Returned"
]

# -----------------------------
# Generate Orders
# -----------------------------

data = []

start_date = datetime(2025, 1, 1)

for i in range(1, 5001):

    customer = random.choice(customers)
    product = random.choice(products)

    order_id = f"ORD{i:05d}"

    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    quantity = random.randint(1, 5)

    discount = random.choice([
        0, 5, 10, 15, 20
    ])

    payment_mode = random.choice(payment_modes)

    order_status = random.choice(order_statuses)

    data.append([
        order_id,
        order_date.strftime("%Y-%m-%d"),

        customer[0],
        customer[1],
        customer[2],
        customer[3],

        product[0],
        product[1],
        product[2],
        quantity,
        product[3],

        discount,
        payment_mode,
        order_status
    ])

# -----------------------------
# Create DataFrame
# -----------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "City",
    "State",
    "Product_ID",
    "Product_Name",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Payment_Mode",
    "Order_Status"
]

df = pd.DataFrame(
    data,
    columns=columns
)

# -----------------------------
# Save CSV
# -----------------------------

df.to_csv(
    "../data/ecommerce_sales.csv",
    index=False
)

print("Dataset created successfully!")

print("Total Records:", len(df))

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nFile saved as:")
print("../data/ecommerce_sales.csv")