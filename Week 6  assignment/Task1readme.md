# Self-Hosted Integration Runtime: Data Extraction from Local SQL Server to Azure SQL Database

This guide outlines the steps to set up a self-hosted integration runtime, extract data from a local SQL Server, and load it into an Azure SQL Database using Azure Data Factory.

## Prerequisites

- Azure Subscription
- Azure Data Factory instance
- Azure SQL Database
- Self-hosted Integration Runtime installed and registered

## Steps

### 1. Set Up Local SQL Database

1. **Create Database and Table**:
   - Open SQL Server Management Studio (SSMS).
   - Execute the following script:

     ```sql
     CREATE DATABASE LocalDB;
     USE LocalDB;

     CREATE TABLE SampleData (
         Id INT PRIMARY KEY,
         Name NVARCHAR(50)
     );

     INSERT INTO SampleData (Id, Name) VALUES (1, 'Example');
     ```

### 2. Set Up Azure SQL Database

1. **Create Azure SQL Database**:
   - In the Azure portal, create a new SQL database named `AzureDB`.

2. **Create Table in Azure SQL Database**:
   - Connect to the Azure SQL Database using SSMS or the Azure portal and run:

     ```sql
     CREATE TABLE SampleData (
         Id INT PRIMARY KEY,
         Name NVARCHAR(50)
     );
     ```

### 3. Install and Register Self-Hosted Integration Runtime

1. **Download and Install**:
   - Download the installer from [Azure Data Factory Integration Runtime](https://go.microsoft.com/fwlink/?linkid=862237).
   - Follow the installation instructions and register the runtime with Azure Data Factory using the runtime key.

### 4. Configure Azure Data Factory

1. **Create Linked Services**:
   - **Local SQL Server**:
     - Navigate to **Manage** > **Linked services**.
     - Create a new linked service for SQL Server and use the self-hosted integration runtime.
   - **Azure SQL Database**:
     - Create a new linked service for Azure SQL Database.

2. **Create Datasets**:
   - **Local SQL Server Dataset**:
     - Point to the `SampleData` table in the local SQL Server.
   - **Azure SQL Database Dataset**:
     - Point to the `SampleData` table in the Azure SQL Database.

3. **Create Pipeline**:
   - **Copy Data Activity**:
     - Create a new pipeline and add a **Copy Data** activity.
     - Set the source to the local SQL Server dataset and the destination to the Azure SQL Database dataset.

### 5. Run and Monitor Pipeline

1. **Validate and Save**:
   - Validate the pipeline to ensure there are no errors.
   - Save the pipeline configuration.

2. **Trigger the Pipeline**:
   - Manually trigger the pipeline from the Azure Data Factory.

3. **Monitor Pipeline**:
   - Check the **Monitor** tab in Azure Data Factory for the pipeline status and logs.

---

This README provides a step-by-step guide for setting up a self-hosted integration runtime and loading data from a local SQL Server to an Azure SQL Database. For more detailed instructions, refer to the official Azure documentation.

---
