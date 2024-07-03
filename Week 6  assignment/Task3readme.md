# Incremental Load Pipeline Setup in Azure Data Factory

This guide provides step-by-step instructions for creating an incremental load pipeline in Azure Data Factory (ADF) and scheduling it to run daily.

## Prerequisites

- An active Azure Subscription
- Azure Data Factory instance
- Source database (e.g., SQL Server, Azure SQL Database) with a table containing a timestamp or ID column for incremental data
- Destination storage (e.g., Azure Blob Storage or Azure SQL Database)

## Steps to Create an Incremental Load Pipeline

### 1. Prepare Source and Destination

#### 1.1. Source Database Setup

1. **Ensure the Source Table is Ready**:
   - The source table should have a timestamp or sequential ID column to identify new or changed rows.
   - Example SQL to create a source table:

     ```sql
     CREATE TABLE SourceTable (
         Id INT PRIMARY KEY,
         Data NVARCHAR(100),
         ModifiedDate DATETIME
     );
     ```

2. **Insert Test Data** (if required):
   
     ```sql
     INSERT INTO SourceTable (Id, Data, ModifiedDate) 
     VALUES (1, 'Initial Data', GETDATE());
     ```

#### 1.2. Destination Storage Setup

1. **Create a Destination Table or Container**:
   - Ensure a destination table or storage is ready to receive data.
   - Example SQL to create a destination table:

     ```sql
     CREATE TABLE DestinationTable (
         Id INT PRIMARY KEY,
         Data NVARCHAR(100),
         ModifiedDate DATETIME
     );
     ```

### 2. Configure Azure Data Factory

#### 2.1. Create Linked Services

1. **Create a Linked Service for the Source**:
   - Navigate to **Manage** > **Linked services** in ADF.
   - Create a new linked service for your source database.

2. **Create a Linked Service for the Destination**:
   - Create another linked service for your destination storage (e.g., Azure Blob Storage or Azure SQL Database).

#### 2.2. Create Datasets

1. **Create a Dataset for the Source**:
   - Go to **Author** > **Datasets** in ADF.
   - Create a dataset for the source table.

2. **Create a Dataset for the Destination**:
   - Create a dataset for the destination table or storage.

#### 2.3. Create the Incremental Load Pipeline

1. **Create a New Pipeline**:
   - Navigate to **Author** > **Pipelines** and create a new pipeline.

2. **Add Lookup Activity**:
   - Add a **Lookup** activity to retrieve the maximum `ModifiedDate` from the destination table.
   - Configure the **Lookup** activity with a query like:

     ```sql
     SELECT MAX(ModifiedDate) AS LastModifiedDate FROM DestinationTable
     ```

3. **Add a Copy Data Activity**:
   - Add a **Copy Data** activity to the pipeline.
   - Configure the source query to select rows where `ModifiedDate` is greater than the `LastModifiedDate` retrieved by the **Lookup** activity:

     ```sql
     SELECT * FROM SourceTable 
     WHERE ModifiedDate > @activity('LookupActivity').output.firstRow.LastModifiedDate
     ```

4. **Set Destination Settings**:
   - Set the destination settings to append new or changed data to the destination table.

### 3. Automate Pipeline Execution

#### 3.1. Create and Configure a Trigger

1. **Create a Daily Trigger**:
   - Go to **Manage** > **Triggers** in ADF.
   - Create a new trigger with a daily recurrence.

2. **Associate the Trigger with the Pipeline**:
   - Go back to the pipeline, click on **Add trigger** > **New/Edit**.
   - Select the newly created trigger and associate it with the pipeline.

### 4. Monitor and Manage the Pipeline

1. **Monitor Pipeline Runs**:
   - Navigate to the **Monitor** tab in ADF to track pipeline runs and check logs.

2. **Handle Errors and Notifications**:
   - Set up alert rules or notifications for pipeline failures or important events.

---

This README provides a concise guide for setting up an incremental load pipeline in Azure Data Factory and automating it for daily execution. 

## References

- [Azure Data Factory Overview](https://docs.microsoft.com/en-us/azure/data-factory/introduction)
- [Incremental Data Loading in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/tutorial-incremental-copy-overview)

