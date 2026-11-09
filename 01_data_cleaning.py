import pandas as pd

# Load dataset
df = pd.read_csv("../data/ecommerce_sales.csv")

print("Original Dataset:")
print(df.head())

print("\nOriginal Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

# Convert numeric columns
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)

df["Discount"] = pd.to_numeric(
    df["Discount"],
    errors="coerce"
)

# Handle missing values
df["Quantity"] = df["Quantity"].fillna(0)

df["Unit_Price"] = df["Unit_Price"].fillna(
    df["Unit_Price"].median()
)

df["Discount"] = df["Discount"].fillna(0)

# Remove invalid records
df = df[df["Quantity"] > 0]
df = df[df["Unit_Price"] > 0]

# Feature engineering
df["Total_Sales"] = (
    df["Quantity"] * df["Unit_Price"]
)

df["Discount_Amount"] = (
    df["Total_Sales"] * df["Discount"] / 100
)

df["Final_Amount"] = (
    df["Total_Sales"] - df["Discount_Amount"]
)

# Date features
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()

# Save cleaned dataset
df.to_csv(
    "../data/cleaned_ecommerce_sales.csv",
    index=False
)

print("\nCleaning Completed Successfully!")

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nFirst 5 Cleaned Records:")
print(df.head())