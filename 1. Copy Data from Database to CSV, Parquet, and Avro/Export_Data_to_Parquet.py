import pyarrow as pa
import pyarrow.parquet as pq
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

# Convert DataFrame to Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, 'employees.parquet')
print("Data exported to employees.parquet")
