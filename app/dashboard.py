import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from scripts.queries import QUERIES

engine = create_engine('sqlite:///RetailSalesDB.db')

st.title("Tableau de bord des ventes au détail")

with engine.connect() as connection:
    total_revenue_query = text(QUERIES["total_revenue"])
    total_revenue = connection.execute(total_revenue_query).fetchone()[0]
    st.metric("Chiffre d'affaires total", f"{total_revenue:,.2f} €")

    category_revenue_query = text(QUERIES["category_revenue"])
    category_revenue = pd.read_sql(category_revenue_query, engine)
    st.bar_chart(category_revenue.set_index("ProductCategory")["Revenue"])

    monthly_revenue_query = text(QUERIES["monthly_revenue"])
    monthly_revenue = pd.read_sql(monthly_revenue_query, engine)
    st.line_chart(monthly_revenue.set_index("Month")["MonthlyRevenue"])