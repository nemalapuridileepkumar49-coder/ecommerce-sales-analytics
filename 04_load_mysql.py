import pandas as pd
import mysql.connector

# --------------------------------
# 1. Read cleaned CSV
# --------------------------------

df = pd.read_csv("../data/cleaned_ecommerce_sales.csv")

# --------------------------------
# 2. Connect to MySQL
# --------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dileep@223005",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")

# --------------------------------
# 3. Insert Customers
# --------------------------------

customers = df[
    ["Customer_ID", "Customer_Name", "City", "State"]
].drop_duplicates()

customer_query = """
INSERT IGNORE INTO customers
(customer_id, customer_name, city, state)
VALUES (%s, %s, %s, %s)
"""

for row in customers.itertuples(index=False, name=None):
    cursor.execute(customer_query, row)

print("Customers inserted:", len(customers))

# --------------------------------
# 4. Insert Products
# --------------------------------

products = df[
    ["Product_ID", "Product_Name", "Category", "Unit_Price"]
].drop_duplicates()

product_query = """
INSERT IGNORE INTO products
(product_id, product_name, category, unit_price)
VALUES (%s, %s, %s, %s)
"""

for row in products.itertuples(index=False, name=None):
    cursor.execute(product_query, row)

print("Products inserted:", len(products))

# --------------------------------
# 5. Insert Orders
# --------------------------------

orders = df[
    [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Payment_Mode",
        "Order_Status"
    ]
].drop_duplicates()

order_query = """
INSERT IGNORE INTO orders
(order_id, order_date, customer_id, payment_mode, order_status)
VALUES (%s, %s, %s, %s, %s)
"""

for row in orders.itertuples(index=False, name=None):
    cursor.execute(order_query, row)

print("Orders inserted:", len(orders))

# --------------------------------
# 6. Insert Order Details
# --------------------------------

details = df[
    [
        "Order_ID",
        "Product_ID",
        "Quantity",
        "Unit_Price",
        "Discount",
        "Total_Sales",
        "Discount_Amount",
        "Final_Amount"
    ]
]

detail_query = """
INSERT INTO order_details
(
    order_id,
    product_id,
    quantity,
    unit_price,
    discount,
    total_sales,
    discount_amount,
    final_amount
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for row in details.itertuples(index=False, name=None):
    cursor.execute(detail_query, row)

print("Order details inserted:", len(details))

# --------------------------------
# 7. Save changes
# --------------------------------

connection.commit()

cursor.close()
connection.close()

print("\nAll data inserted successfully!")