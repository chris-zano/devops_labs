### Managing System Services and Temporary Files

This Python script demonstrates how to manage system services and handle temporary folders using the `os`, `subprocess`, and `shutil` modules.

#### Overview

1. **Restart a Service**: The script includes a function to restart a system service using `systemctl`.
2. **Clear a Temporary Folder**: The script clears and re-creates a temporary folder for reuse.

#### Modules Used

- **`os`**: Used for file and directory operations.
- **`subprocess`**: Allows running system commands.
- **`shutil`**: Provides high-level file operations, including deleting directories.

---

### Code Details

#### Function: `restart_service`

**Purpose**: Restarts a specified system service using `systemctl`.

##### Parameters:
- `service_name` (str): The name of the service to restart.

##### Example:
```python
def restart_service(service_name):
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)
        print(f"Service '{service_name}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting service '{service_name}': {e}")
```

##### Usage:
```python
SERVICE_NAME = "cron"
restart_service(SERVICE_NAME)
```
This will restart the `cron` service. Ensure the script is run with sufficient permissions.

---

#### Function: `clear_temp_folder`

**Purpose**: Deletes all contents of a specified folder and re-creates it.

##### Parameters:
- `temp_folder` (str): The path to the temporary folder.

##### Example:
```python
def clear_temp_folder(temp_folder):
    try:
        shutil.rmtree(temp_folder)
        os.makedirs(temp_folder)
        print(f"Temporary folder '{temp_folder}' cleared successfully.")
    except Exception as e:
        print(f"Error clearing temporary folder '{temp_folder}': {e}")
```

##### Usage:
```python
TEMP_FOLDER = "/tmp/test_folder"
clear_temp_folder(TEMP_FOLDER)
```
This deletes all contents of `/tmp/test_folder` and ensures the folder is re-created.

---
### Notes

1. **Passwordless `sudo` for `cron`**: To restart the `cron` service without being prompted for a password, the script requires a modification to the `sudoers` file. I used the following command to edit it:  
   ```bash
   sudo visudo
   ```
   Added the following line to allow passwordless `sudo` for restarting `cron`:  
   ```plaintext
   my_username ALL=(ALL) NOPASSWD: /bin/systemctl restart cron
   ```

2. **Error Handling**: Both functions include basic error handling to ensure issues are logged to the console, making debugging easier.
