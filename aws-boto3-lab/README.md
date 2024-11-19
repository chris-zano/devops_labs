# AWS Boto3 Lab

## Project Objective
The **AWS Boto3 Lab** project is designed for learning how to interact with AWS resources programmatically using the **Boto3 API**. It provides hands-on experience in managing AWS services like **S3** and **EC2**.

---

## Project Structure
This project has the following structure:

- **`main.py`**: Entry point of the project, demonstrating how to use the `S3Manager` and `EC2Manager` classes.
- **`s3manager.py`**: Contains the `S3Manager` class to manage AWS S3 operations.
- **`ec2manager.py`**: Contains the `EC2Manager` class to manage AWS EC2 operations.

---

## Detailed Modules

### `s3manager.py`
#### `class S3Manager`
Provides utility functions for interacting with S3 resources.

- **`__init__(self, session)`**
  - Initializes the `S3Manager` with a Boto3 session.

- **`list_buckets(self)`**
  - Lists all S3 buckets available in the AWS account associated with the session.

- **`upload_file(self, bucket_name, file_name, object_name)`**
  - Uploads a file to the specified S3 bucket.
  - **Parameters**:
    - `bucket_name`: Name of the target bucket.
    - `file_name`: Path to the file to be uploaded.
    - `object_name`: S3 object name after upload.

---

### `ec2manager.py`
#### `class EC2Manager`
Provides functionality for managing EC2 instances.

- **`__init__(self, client)`**
  - Initializes the `EC2Manager` with a Boto3 EC2 client.
  - Caches EC2 data for repeated queries.

- **`list(self)`**
  - Retrieves and caches EC2 instance descriptions.
  - Returns a JSON-like structure containing instance details.

---

### `main.py`
Demonstrates the use of `S3Manager` and `EC2Manager` classes:
1. **S3 Operations**:
   - List all S3 buckets.
   - Upload a file (`test.txt`) to a specified S3 bucket.

2. **EC2 Operations**:
   - List EC2 instances and save the details to `instances.json`.

---

## Prerequisites

1. **AWS Credentials**: Configure AWS credentials (Access Key, Secret Key, and Region) using environment variables or an AWS profile. Example:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=your_region
   ```

2. **Python**: Ensure Python 3.x is installed along with Boto3. Install dependencies using:
   ```bash
   pip install boto3
   ```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/aws-boto3-lab.git
   cd aws-boto3-lab
   ```

2. Run the script:
   ```bash
   python main.py
   ```

---

## Output
- **S3 Bucket List**: Displays all buckets in the AWS account.
- **File Upload**: Uploads `test.txt` to the specified S3 bucket.
- **EC2 Instances List**: Saves details of EC2 instances in `instances.json`.

---

## Notes
- Modify the `bucket_name` and `file_name` in `main.py` to match your AWS setup.
- Ensure the specified S3 bucket exists and is accessible.
- Handle exceptions for scenarios like invalid AWS credentials, nonexistent buckets, or unauthorized access.