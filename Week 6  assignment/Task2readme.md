# Configure FTP/SFTP Server and Create ADF Pipeline for Data Extraction

This guide provides instructions for setting up an FTP/SFTP server and creating an Azure Data Factory (ADF) pipeline for data extraction.

## Prerequisites

- FTP/SFTP Server software (e.g., FileZilla Server for FTP, OpenSSH for SFTP)
- Azure Subscription
- Azure Data Factory instance
- Azure storage destination (e.g., Azure Blob Storage or Azure SQL Database)

## Steps

### 1. Set Up FTP/SFTP Server

#### 1.1 FTP Server (FileZilla)

1. **Download and Install FileZilla Server**:
   - Download from [FileZilla Server](https://filezilla-project.org/download.php?type=server).
   - Follow the installation instructions.

2. **Create a User and Set Directory**:
   - Open FileZilla Server, go to **Edit** > **Users**.
   - Add a new user and set a password.
   - Configure a home directory for file storage.

3. **Start the FTP Server**:
   - Start the server, noting the IP address and port (default is `21`).

#### 1.2 SFTP Server (OpenSSH)

1. **Install OpenSSH**:
   - On Windows, add OpenSSH via Settings > Apps > Optional Features.
   - On Linux, install using: `sudo apt-get install openssh-server`.

2. **Create a User and Set Directory**:
   - Add a user for SFTP and set up their home directory.

3. **Configure SSH**:
   - Edit `/etc/ssh/sshd_config` to enable SFTP by adding:

     ```shell
     Subsystem sftp /usr/lib/openssh/sftp-server
     ```

4. **Start the SFTP Server**:
   - Restart the SSH service with: `sudo service ssh restart`.

### 2. Configure Azure Data Factory

#### 2.1 Create Linked Services

1. **FTP/SFTP Linked Service**:
   - Go to Azure Data Factory > **Manage** > **Linked services**.
   - Create a new linked service for FTP or SFTP.
   - Enter connection details (IP address, port, username, password).

2. **Azure Storage Linked Service**:
   - Create a linked service for your Azure storage destination.

#### 2.2 Create Datasets

1. **FTP/SFTP Dataset**:
   - Navigate to **Author** > **Datasets**.
   - Create a dataset pointing to the FTP/SFTP server directory with the data.

2. **Destination Dataset**:
   - Create a dataset pointing to your Azure storage destination.

#### 2.3 Create Pipeline

1. **Copy Data Activity**:
   - Go to **Author** > **Pipelines** and create a new pipeline.
   - Add a **Copy Data** activity to the pipeline.
   - Set the source to the FTP/SFTP dataset and the sink to the Azure storage dataset.

### 3. Run and Monitor Pipeline

1. **Validate and Save**:
   - Validate the pipeline to check for errors.
   - Save the pipeline configuration.

2. **Trigger the Pipeline**:
   - Manually trigger the pipeline in Azure Data Factory.

3. **Monitor the Pipeline**:
   - Use the **Monitor** tab in Azure Data Factory to check the status and logs.

---

This README provides a quick guide to set up an FTP/SFTP server and create an ADF pipeline for data extraction. For more detailed instructions, refer to Azure documentation.
