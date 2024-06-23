import pyodbc
import pandas as pd

# Database connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-L5DILJH\\SQLEXPRESS;'
    'DATABASE=db_assignment5;'
    'UID=yours_Radha-Krishna;'
    'PWD=Radha-Krishna#123*'
)

# Query data
query = "SELECT * FROM Employees"
df = pd.read_sql(query, conn)

# Export to CSV
df.to_csv('employees.csv', index=False)
conn.close()
print("Data exported to employees.csv")
