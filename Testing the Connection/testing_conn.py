import pyodbc
import pandas as pd
conn=None
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-L5DILJH\\SQLEXPRESS;'
        'DATABASE=db_assignment5;'
        'UID=yours_Radha-Krishna;'
        'PWD=Radha-Krishna#123*'
    )
    print("Connection successful")
    query = "SELECT * FROM Employees"
    df = pd.read_sql(query, conn)
    print(df.head())

except Exception as e:
    print(f"Error: {e}")

finally:
    if conn:
        conn.close()
        print("Connection closed")
