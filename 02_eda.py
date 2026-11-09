import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Cleaned Dataset
# -----------------------------

df = pd.read_csv(
    "../data/cleaned_ecommerce_sales.csv"
)

print("Cleaned Dataset:")
print(df.head())

# -----------------------------
# 2. Basic Business Metrics
# -----------------------------

total_revenue = df["Final_Amount"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_ID"].nunique()

total_products = df["Product_ID"].nunique()

average_order_value = (
    total_revenue / total_orders
)

print("\n========== BUSINESS METRICS ==========")

print("Total Revenue:", total_revenue)

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

print("Total Products:", total_products)

print("Average Order Value:", average_order_value)

# -----------------------------
# 3. Category Analysis
# -----------------------------

category_sales = (
    df.groupby("Category")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY SALES ==========")
print(category_sales)

# -----------------------------
# 4. State Analysis
# -----------------------------

state_sales = (
    df.groupby("State")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== STATE SALES ==========")
print(state_sales)

# -----------------------------
# 5. Top 10 Products
# -----------------------------

top_products = (
    df.groupby("Product_Name")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products)

# -----------------------------
# 6. Payment Mode Analysis
# -----------------------------

payment_analysis = (
    df.groupby("Payment_Mode")["Final_Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== PAYMENT MODE SALES ==========")
print(payment_analysis)

# -----------------------------
# 7. Order Status Analysis
# -----------------------------

order_status = (
    df["Order_Status"]
    .value_counts()
)

print("\n========== ORDER STATUS ==========")
print(order_status)

# -----------------------------
# 8. Monthly Sales
# -----------------------------

monthly_sales = (
    df.groupby("Month")["Final_Amount"]
    .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# -----------------------------
# 9. Category Chart
# -----------------------------

category_sales.plot(
    kind="bar",
    title="Sales by Category"
)

plt.xlabel("Category")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

# -----------------------------
# 10. Top Products Chart
# -----------------------------

top_products.plot(
    kind="bar",
    title="Top 10 Products"
)

plt.xlabel("Product")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# 11. Monthly Sales Chart
# -----------------------------

monthly_sales.plot(
    kind="line",
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()

print("\nEDA Completed Successfully!")