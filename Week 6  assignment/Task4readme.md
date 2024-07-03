# Automate a Pipeline to Trigger Every Last Saturday of the Month

This guide provides instructions to automate an Azure Data Factory (ADF) pipeline to trigger every last Saturday of the month.

## Prerequisites

- Azure Subscription
- Azure Data Factory instance
- An existing pipeline in ADF

## Steps

### 1. Create a Pipeline

1. **Navigate to Azure Data Factory**:
   - Open the Azure portal and go to your Azure Data Factory instance.

2. **Create or Select a Pipeline**:
   - Go to **Author** > **Pipelines**.
   - Create a new pipeline or select an existing one that you want to trigger every last Saturday of the month.

### 2. Create a Custom Trigger

#### 2.1. Define the Trigger

1. **Go to Triggers**:
   - Navigate to **Manage** > **Triggers**.

2. **Add a New Trigger**:
   - Click on **New** to create a new trigger.

3. **Configure the Trigger**:
   - Name your trigger (e.g., `LastSaturdayOfMonthTrigger`).
   - Set the **Type** to **Schedule**.

4. **Set Schedule**:
   - In the **Schedule** section, set the **Start Date** to the first day of the month and **Start Time** to the desired time for the trigger.
   - Set **Recurrence** to **Monthly** with an interval of `1`.

#### 2.2. Add Custom Logic for Last Saturday

1. **Create a Tumbling Window**:
   - Set up a tumbling window with a **Size** of `1 Month`.
   - Add a **Window start** condition to ensure that the pipeline only runs if today is the last Saturday of the month.
   - Use a custom script to check if today is the last Saturday of the month.


### 3. Associate the Trigger with the Pipeline

1. **Go Back to the Pipeline**:
   - Go back to your pipeline in **Author** > **Pipelines**.

2. **Add Trigger to the Pipeline**:
   - Click on **Add trigger** > **New/Edit**.
   - Select the trigger you just created (`LastSaturdayOfMonthTrigger`).

3. **Save and Publish**:
   - Save your changes and click **Publish** to apply the new trigger configuration.

### 4. Monitor the Trigger

1. **Monitor Pipeline Runs**:
   - Use the **Monitor** tab in ADF to track the pipeline execution and ensure that it runs as expected every last Saturday of the month.

2. **Check for Errors and Notifications**:
   - Configure alerts or notifications to stay informed about the status of the pipeline and any errors that may occur.

---

This README provides a concise guide to setting up a trigger in Azure Data Factory that will run a pipeline on the last Saturday of every month. 

## References

- [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/)
- [Create Schedule Triggers](https://docs.microsoft.com/en-us/azure/data-factory/how-to-create-schedule-trigger)
