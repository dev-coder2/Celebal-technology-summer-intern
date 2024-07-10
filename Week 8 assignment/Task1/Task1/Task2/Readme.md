# Azure Data Services Task: Load, Flatten JSON, and Write as Parquet

This guide outlines the steps to load a dataset into Azure Blob Storage or Data Lake, flatten JSON fields using Azure Data Factory (ADF) Data Flow, and write the flattened data as an external Parquet table.

## Steps

### 1. Load Dataset into Azure Blob Storage or Data Lake

1. **Upload Dataset**: Upload your dataset (e.g., CSV, JSON) to Azure Blob Storage or Data Lake Storage using Azure Portal or Azure CLI.

### 2. Flatten JSON Fields using Azure Data Factory Data Flow

1. **Create Azure Data Factory**: Set up an Azure Data Factory instance in the Azure Portal.

2. **Create Data Flow**: 
   - Navigate to the Data Factory UI.
   - Create a new Data Flow.
   - Add a source dataset pointing to your uploaded file in Azure Blob Storage or Data Lake.
   - Use the "Flatten" transformation to expand nested JSON structures into individual columns.
   - Map the fields you want to extract from the JSON structure.

### 3. Write Flattened Data as External Parquet Table

1. **Configure Sink**: 
   - Add a sink dataset pointing to a destination in Azure Blob Storage or Data Lake where you want to store the flattened data.
   - Specify Parquet as the output format.

2. **Set Sink Properties**: 
   - Configure partitioning, file naming conventions, and any additional settings as required.

## Summary

This process enables you to preprocess and store structured or semi-structured data efficiently using Azure Blob Storage or Data Lake and Azure Data Factory. Flattening JSON fields ensures that nested data structures are simplified for downstream analytics or machine learning tasks.



