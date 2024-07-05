# Azure Data Integration Project

## Objective
To integrate and manage data from Oracle (on-premise), Salesforce, and semi-structured files on FTP into Azure for efficient data processing, storage, and analytics.

## Data Sources

### 1. Oracle (On-Premise)
- **Monthly Incremental Data Size**: 30 GB
- **Total Table Count**: 20

### 2. Salesforce
- **Monthly Incremental Data Size**: 50 GB
- **Total Table Count**: 120

### 3. Semi-structured Files on FTP
- **Monthly Data Size**: 5 GB
- **Approximate File Count per Month**: 20

## Azure Services and Components

### 1. Azure Data Factory (ADF)
**Purpose**: Data orchestration and automation for ETL processes.

- **Integration Runtimes**:
  - **Self-hosted IR**: Connect to Oracle (on-premise) for secure data transfer.
  - **Azure IR**: Connect to Salesforce and FTP for data extraction.
- **Pipelines**: Create pipelines for extracting, transforming, and loading data.
- **Activities**: Use Copy activities for data movement.

### 2. Azure SQL Database
**Purpose**: Storage and management of structured data.

- **Databases**: Separate databases for Oracle and Salesforce data.
- **Tables**: Create tables matching the source schema.
- **Scaling and Backup**: Automated scaling and backup.

### 3. Azure Blob Storage
**Purpose**: Storage for semi-structured files.

- **Containers**: Organize files in containers based on file type and source.
- **Data Lake**: Use Azure Data Lake Storage Gen2 for hierarchical storage.

### 4. Azure Synapse Analytics
**Purpose**: Data integration and analytics.

- **SQL Pools**: Use dedicated SQL pools for data warehousing.
- **Data Integration**: Combine data from Azure SQL Database and Blob Storage.

### 5. Azure Key Vault
**Purpose**: Secure management of secrets and keys.

- **Secrets**: Store connection strings and passwords.
- **Keys**: Manage encryption keys securely.

### 6. Azure Monitor and Log Analytics
**Purpose**: Monitoring and logging of Azure services.

- **Metrics**: Set up monitoring for data pipelines and services.
- **Logs**: Collect and analyze logs for diagnostics and performance.

## Implementation Steps

1. **Set up Azure Data Factory**:
   - Create pipelines for data ingestion.
   - Configure Integration Runtimes for connecting to data sources.

2. **Configure Azure SQL Database**:
   - Set up databases and tables for structured data storage.
   - Implement automated scaling and backup policies.

3. **Set up Azure Blob Storage**:
   - Create containers and configure access policies for semi-structured files.

4. **Integrate with Azure Synapse Analytics**:
   - Set up data warehousing and analytics.
   - Integrate data from Azure SQL Database and Blob Storage.

5. **Secure with Azure Key Vault**:
   - Store and manage secrets and keys securely.

6. **Enable Monitoring and Logging**:
   - Configure Azure Monitor and Log Analytics for continuous monitoring.

## Cost Estimation
Estimated costs are based on data volume and service usage:

- **Azure Data Factory**: Costs for pipeline runs and data movement.
- **Azure SQL Database**: Storage and compute costs.
- **Azure Blob Storage**: Storage costs for semi-structured files.
- **Azure Synapse Analytics**: Data warehousing and analytics costs.
- **Azure Key Vault**: Secret and key management costs.
- **Azure Monitor**: Costs for monitoring and log storage.



## Conclusion
This document outlines a comprehensive Azure BoM for integrating and managing data from Oracle, Salesforce, and semi-structured files on FTP, providing a scalable and secure solution for data processing and analytics.
