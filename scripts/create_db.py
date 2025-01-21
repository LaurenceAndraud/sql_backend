from sqlalchemy import create_engine, text
import pandas as pd

# Load data
data = pd.read_csv("retail_sales_dataset.csv")

data.rename(columns={
    "Transaction ID": "TransactionID",
    "Date": "TransactionDate",
    "Customer ID": "CustomerID",
    "Gender": "Gender",
    "Age": "Age",
    "Product Category": "ProductCategory",
    "Quantity": "Quantity",
    "Price per Unit": "PricePerUnit",
    "Total Amount": "TotalAmount"
}, inplace=True)

data["TransactionDate"] = pd.to_datetime(data["TransactionDate"], errors="coerce").dt.date

# Connect to the sqlite base
engine = create_engine("sqlite:///RetailSalesDB.db")

# Execut query
with engine.connect() as connection:
    connection.execute(text("""
    CREATE TABLE IF NOT EXISTS RetailSales (
        TransactionID INT PRIMARY KEY,
        TransactionDate DATE,
        CustomerID VARCHAR(20),
        Gender VARCHAR(10),
        Age INT,
        ProductCategory VARCHAR(50),
        Quantity INT,
        PricePerUnit DECIMAL(10, 2),
        TotalAmount DECIMAL(10, 2)
    );
    """))

# Insert data
data.to_sql("RetailSales", con=engine, if_exists='append', index=False)
print("Data insert with success !")