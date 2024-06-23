import fastavro

# Read and print the Avro file contents
with open('employees.avro', 'rb') as f:
    reader = fastavro.reader(f)
    for record in reader:
        print(record)
