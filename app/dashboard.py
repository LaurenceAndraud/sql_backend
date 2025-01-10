import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from scripts.queries import QUERIES

engine = create_engine('sqlite:///RetailSalesDB.db')

st.title("Tableau de bord des ventes au détail")

with engine.connect() as connection:
    total_revenue = connection.execute(QUERIES["total_revenue"]).fetchone()[0]
st.metric("Chiffre d'affaires total", f"{total_revenue:,.2f} €")
category_revenue = pd.read_sql(QUERIES["category_revenue"], engine)
st.bar_chart(category_revenue.set_index("ProductCategory")["Revenue"])
monthly_revenue = pd.read_sql(QUERIES["monthly_revenue"], engine)
st.line_chart(monthly_revenue.set_index("Month")["MonthlyRevenue"])