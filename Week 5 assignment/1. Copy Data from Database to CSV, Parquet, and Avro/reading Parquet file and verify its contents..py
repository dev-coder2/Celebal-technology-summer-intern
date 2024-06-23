import pyarrow.parquet as pq

# Read the Parquet file
table = pq.read_table('employees.parquet')
df = table.to_pandas()

# Print the DataFrame
print(df)