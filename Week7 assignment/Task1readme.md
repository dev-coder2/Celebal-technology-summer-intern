# Azure Data Factory Pipelines for File Ingestion and Processing

## Overview

This guide outlines the setup of Azure Data Factory (ADF) pipelines to ingest and process different types of files from Azure Data Lake Storage into Azure SQL Database tables.

### Task

The task involves fetching three types of files from an Azure Data Lake container and loading them into their respective tables:

1. **CUST_MSTR Files**: Extract date from filename and load into the `CUST_MSTR` table.
2. **master_child_export Files**: Extract date and date key from filename and load into the `master_child` table.
3. **H_ECOM_ORDER Files**: Load directly into the `H_ECOM_Orders` table.

## Prerequisites

- Azure Subscription
- Azure Data Factory instance
- Access to Azure Data Lake Storage Gen2
- Azure SQL Database instance

## Steps to Implement

### 1. Set Up Linked Services

1. **Azure Storage Linked Service**:
   - Create a linked service for Azure Data Lake Storage where the files are stored.

2. **Azure SQL Database Linked Service**:
   - Create a linked service for Azure SQL Database where the target tables (`CUST_MSTR`, `master_child`, `H_ECOM_Orders`) exist.

### 2. Define Datasets

1. **Data Lake Storage Datasets**:
   - Create datasets for each file type (`CUST_MSTR`, `master_child_export`, `H_ECOM_ORDER`) pointing to their respective folders in Azure Data Lake Storage.

2. **Azure SQL Database Datasets**:
   - Create datasets for each target table (`CUST_MSTR`, `master_child`, `H_ECOM_Orders`) in Azure SQL Database.

### 3. Configure Pipelines

#### Pipeline 1: Load CUST_MSTR Files

1. **Copy Data Activity**:
   - Source: Data Lake Storage dataset for `CUST_MSTR_*`.
   - Destination: Azure SQL Database dataset for `CUST_MSTR` table.
   - Use a derived column to extract the date from the filename and format it (`yyyy-MM-dd`).
   
     **Derived Column Expression:**
     ```json
     iif(startsWith(item().name, 'CUST_MSTR'), toDate(substring(item().name, 9, 8)), null)
     ```
     - `substring(item().name, 9, 8)`: Extracts the date part (`YYYYMMDD`) from the filename starting at index 9.
     - `toDate(...)`: Converts the extracted substring into a date format.

   - Load data into `CUST_MSTR` table, appending new data daily.

#### Pipeline 2: Load master_child_export Files

1. **Copy Data Activity**:
   - Source: Data Lake Storage dataset for `master_child_export-*`.
   - Destination: Azure SQL Database dataset for `master_child` table.
   - Use derived columns to extract and format `date` (`yyyy-MM-dd`) and `datekey` (`yyyyMMdd`) from the filename.
   
     **Derived Column Expressions:**
     - For `date`:
       ```json
       iif(startsWith(item().name, 'master_child_export'), toDate(substring(item().name, 21, 8)), null)
       ```
     - For `datekey`:
       ```json
       iif(startsWith(item().name, 'master_child_export'), substring(item().name, 21, 8), null)
       ```

   - Load data into `master_child` table, appending new data daily.

#### Pipeline 3: Load H_ECOM_ORDER Files

1. **Copy Data Activity**:
   - Source: Data Lake Storage dataset for `H_ECOM_ORDER.csv`.
   - Destination: Azure SQL Database dataset for `H_ECOM_Orders` table.
   - Load data directly into `H_ECOM_Orders` table, overwriting existing data daily.

### 4. Schedule Triggers

1. **Set Daily Triggers**:
   - Schedule each pipeline to run daily to ensure data is processed and loaded regularly.

### 5. Monitoring and Error Handling

1. **Monitor Pipeline Runs**:
   - Use Azure Data Factory Monitoring to track pipeline executions and verify data loads.

2. **Implement Error Handling**:
   - Configure retry policies and error notifications to handle pipeline failures effectively.

---

By following these steps, you can automate the ingestion and processing of various file types into Azure SQL Database tables using Azure Data Factory. Adjust configurations based on your specific file naming conventions and data requirements.

For detailed guidance, refer to the [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/).
