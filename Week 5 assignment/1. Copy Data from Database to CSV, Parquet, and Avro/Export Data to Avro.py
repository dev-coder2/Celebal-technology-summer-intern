import pyodbc
import pandas as pd
import fastavro

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

# Convert date fields to string
df['DateOfBirth'] = df['DateOfBirth'].astype(str)
df['HireDate'] = df['HireDate'].astype(str)

# Define Avro schema
schema = {
    'doc': 'Employees',
    'name': 'Employee',
    'namespace': 'example.avro',
    'type': 'record',
    'fields': [
        {'name': 'EmployeeID', 'type': 'int'},
        {'name': 'FirstName', 'type': 'string'},
        {'name': 'LastName', 'type': 'string'},
        {'name': 'Email', 'type': 'string'},
        {'name': 'DateOfBirth', 'type': 'string'},
        {'name': 'JobTitle', 'type': 'string'},
        {'name': 'Salary', 'type': 'float'},
        {'name': 'HireDate', 'type': 'string'}
    ]
}

# Write to Avro file
with open('employees.avro', 'wb') as out:
    fastavro.writer(out, schema, df.to_dict(orient='records'))
print("Data exported to employees.avro")
