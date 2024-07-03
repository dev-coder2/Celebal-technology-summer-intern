# Retrieving Data with Azure Data Factory

This guide provides instructions for setting up an Azure Data Factory (ADF) pipeline to retrieve data from a source and handle it appropriately.

## Prerequisites

- Azure Subscription
- Azure Data Factory instance
- Access to the source data (e.g., SQL Server, FTP, Blob Storage)

## Steps to Retrieve Data

### 1. Set Up Your Data Source

1. **Identify Your Data Source**:
   - Determine the data source type (e.g., SQL Server, FTP, Blob Storage).

2. **Ensure Access**:
   - Make sure you have access credentials and necessary permissions to retrieve data from the source.

### 2. Configure Azure Data Factory

#### 2.1. Create Linked Services

1. **Source Linked Service**:
   - Go to **Manage** > **Linked services** in ADF.
   - Click on **New** to create a linked service for your source data.
   - Fill in the required details (e.g., server name, credentials, storage account).

   ![Create Linked Service](https://docs.microsoft.com/en-us/azure/data-factory/media/quickstart-create-data-factory-portal/linked-service.png)

2. **Destination Linked Service** (if needed):
   - Create a linked service for your destination storage (e.g., Azure SQL Database, Blob Storage).

#### 2.2. Create Datasets

1. **Source Dataset**:
   - Navigate to **Author** > **Datasets**.
   - Click on **New dataset** and choose the appropriate format (e.g., SQL, Blob, FTP).
   - Configure it to point to your data source.

2. **Destination Dataset** (if needed):
   - Create a dataset for your destination where the data will be stored.

#### 2.3. Create the Data Retrieval Pipeline

1. **Create a New Pipeline**:
   - Navigate to **Author** > **Pipelines**.
   - Click on **New pipeline** to create a new data pipeline.

2. **Add a Source Activity**:
   - Add a **Copy Data** activity to the pipeline.
   - Set the source to your **Source Dataset**.

3. **Configure Data Retrieval**:
   - Configure the **Copy Data** activity to retrieve data from the source.
   - Set up any required parameters or filters for data extraction.

4. **Set Destination (Optional)**:
   - If you are moving data to a new location, set the destination to your **Destination Dataset**.

   ![Pipeline Configuration](https://docs.microsoft.com/en-us/azure/data-factory/media/quickstart-create-data-factory-portal/pipeline.png)

### 3. Test and Validate the Pipeline

1. **Validate Pipeline**:
   - Click on **Validate** in the pipeline editor to check for any configuration errors.

2. **Test the Pipeline**:
   - Click on **Debug** to run the pipeline and ensure it retrieves data as expected.

### 4. Schedule the Pipeline

1. **Create a Trigger**:
   - Go to **Manage** > **Triggers**.
   - Click on **New** to create a new trigger.

2. **Configure Trigger Schedule**:
   - Set up the trigger to run the pipeline at desired intervals (e.g., daily, weekly).
   - Ensure it aligns with your data retrieval needs.

3. **Associate Trigger with Pipeline**:
   - Go back to the pipeline, click on **Add trigger** > **New/Edit**.
   - Select the trigger you created and associate it with the pipeline.

### 5. Monitor the Pipeline

1. **Monitor Pipeline Runs**:
   - Use the **Monitor** tab in ADF to check the status of pipeline runs and view logs for any errors.

2. **Set Up Alerts**:
   - Configure alerts or notifications to get updates on pipeline execution status or failures.

### Additional Notes

- **Handle Large Data**: If dealing with large data, consider setting up chunking or pagination to handle data in manageable sizes.
- **Error Handling**: Implement error handling and retry mechanisms within your pipeline to manage failures.

---

This README provides a concise guide to setting up and automating a data retrieval pipeline in Azure Data Factory.

## References

- [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/)
- [Creating Pipelines in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/tutorial-pipeline-copy-data)
- [Scheduling Triggers in Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/how-to-create-schedule-trigger)
