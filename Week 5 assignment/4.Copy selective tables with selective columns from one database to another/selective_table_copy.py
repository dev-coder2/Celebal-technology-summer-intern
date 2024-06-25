import pyodbc

def copy_tables_and_columns(source_conn_str, target_conn_str, tables_columns_mapping):
    # Connect to the source and target databases
    source_conn = pyodbc.connect(source_conn_str)
    target_conn = pyodbc.connect(target_conn_str)
    
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    for source_table, columns_to_copy in tables_columns_mapping.items():
        print(f"Copying table: {source_table}")

        # Generate SELECT statement for specified columns
        select_columns = ', '.join(columns_to_copy)
        select_sql = f"SELECT {select_columns} FROM {source_table}"

        # Retrieve data from source table
        source_cursor.execute(select_sql)
        rows = source_cursor.fetchall()

        # Create table in target database
        create_table_sql = f"CREATE TABLE {source_table} ({', '.join([f'{col} NVARCHAR(MAX)' for col in columns_to_copy])})"
        try:
            target_cursor.execute(create_table_sql)
            print(f"Created table {source_table} in target database.")
        except Exception as e:
            print(f"Error creating table {source_table}: {e}")

        # Insert data into target table
        if rows:
            placeholders = ', '.join(['?'] * len(columns_to_copy))
            insert_sql = f"INSERT INTO {source_table} ({', '.join(columns_to_copy)}) VALUES ({placeholders})"
            
            for row in rows:
                try:
                    target_cursor.execute(insert_sql, row)
                except Exception as e:
                    print(f"Error inserting data into table {source_table}: {e}")

    # Commit the transaction
    target_conn.commit()

    # Close the connections
    source_cursor.close()
    target_cursor.close()
    source_conn.close()
    target_conn.close()

# Example connection strings for source and target databases
source_connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-L5DILJH\\SQLEXPRESS;"
    "DATABASE=db_source;"
    "UID=your_dbsource;"
    "PWD=db_source123#;"
)

target_connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-L5DILJH\\SQLEXPRESS;"
    "DATABASE=db_target;"
    "UID=your_dbtarget;"
    "PWD=db_target123#;"
)

# Specify tables and columns to copy
# Format: {'source_table': ['column1', 'column2', ...]}
tables_columns_mapping = {
    'customers': ['customer_id', 'first_name','last_name','email','phone'],
    'orders': ['order_id', 'customer_id', 'total_amount'],
    'products':['product_id', 'product_name']
}

# Call the function to copy tables and columns
copy_tables_and_columns(source_connection_string, target_connection_string, tables_columns_mapping)
