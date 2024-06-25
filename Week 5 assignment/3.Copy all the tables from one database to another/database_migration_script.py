import pyodbc

def copy_tables(source_conn_str, target_conn_str, table_names):
    # Connect to the source and target databases
    source_conn = pyodbc.connect(source_conn_str)
    target_conn = pyodbc.connect(target_conn_str)
    
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()

    for table_name in table_names:
        print(f"Copying table: {table_name}")

        # Get the columns and data from the source table
        source_cursor.execute(f"SELECT * FROM {table_name}")
        rows = source_cursor.fetchall()
        columns = [column[0] for column in source_cursor.description]

        # Create table in the target database
        columns_definition = ', '.join([f"{col} NVARCHAR(MAX)" for col in columns])
        create_table_sql = f"CREATE TABLE {table_name} ({columns_definition})"
        try:
            target_cursor.execute(create_table_sql)
            print(f"Created table {table_name} in target database.")
        except Exception as e:
            print(f"Error creating table {table_name}: {e}")

        # Insert data into the target table
        if rows:
            columns_placeholder = ', '.join(columns)
            placeholders = ', '.join(['?'] * len(columns))
            insert_sql = f"INSERT INTO {table_name} ({columns_placeholder}) VALUES ({placeholders})"
            
            for row in rows:
                try:
                    target_cursor.execute(insert_sql, row)
                except Exception as e:
                    print(f"Error inserting data into table {table_name}: {e}")

    # Commit the transaction
    target_conn.commit()

    # Close the connections
    source_cursor.close()
    target_cursor.close()
    source_conn.close()
    target_conn.close()

# Connection strings for source and target databases
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

# List of tables to copy
table_names = ["customers", "orders", "products"]

# Call the function to copy tables
copy_tables(source_connection_string, target_connection_string, table_names)
