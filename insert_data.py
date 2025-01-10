from sqlalchemy import create_engine
import pandas as pd

# Load data
data = pd.read_csv("retail_sales_dataset.csv")

# Connect to the sqlite base
engine = create_engine("sqlite:///RetailSalesDB.db")

# Execut query
with engine.connect() as connection:
    connection.execute("""
    CREATE TABLE RetailSales (
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
    """)