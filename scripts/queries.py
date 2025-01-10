## TOTAL CA ##
query_total_revenue = '''
SELECT SUM(TotalAmount) AS TotalRevenue
FROM RetailSales;
'''

## SALES PER CATEGORY ##
query_category_revenue = '''
SELECT ProductCategory, SUM (TotalAmount) AS Revenue
FROM RetailSales
GROUP BY ProductCategory
ORDER BY Revenue DESC;
'''

## MENSUAL SALES ##
query_monthly_revenue = '''
SELECT strftime('%Y-%m', TransactionDate) AS Month, SUM(TotalAmount) AS MonthlyRevenue
FROM RetailSales
GROUP BY Month
ORDER BY Month;
'''

# Export queries as dictionnary
QUERIES = {
    "total_revenue": query_total_revenue,
    "category_revenue": query_category_revenue,
    "monthly_revenue": query_monthly_revenue,
}