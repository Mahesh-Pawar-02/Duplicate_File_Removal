# DuplicateFileRemoval

## Description
This script, DuplicateFileRemoval.py, automates the process of identifying and deleting duplicate files within a specified directory. It also logs the names of the deleted files and emails the log file to a specified recipient. The log file includes statistics about the operation, such as the total number of files scanned and the number of duplicates found. The script is designed to run at specified intervals.

## Command Line Options
- `DuplicateFileRemoval.py <directory_path> <interval_minutes> <email_id>`
  - `<directory_path>`: Absolute path of the directory which may contain duplicate files.
  - `<interval_minutes>`: Time interval in minutes after which the script performs the duplicate file removal.
  - `<email_id>`: Email ID of the receiver for the log file.

## Usage
python DuplicateFileRemoval.py E:/Data/Demo 50 admin123@gmail.com


## Dependencies
- `hashlib`
- `os`
- `time`
- `smtplib`
- `email`
- `argparse`
- `schedule`

#### *Features*

1. *Duplicate File Removal*:
   - Scans the specified directory for duplicate files based on checksum.
   - Deletes the duplicate files and logs their names.

2. *Logging*:
   - Creates a log file in the "Marvellous" directory.
   - Log file name includes the date and time of creation.
   - Logs contain the names of the deleted duplicate files.

3. *Scheduled Execution*:
   - Runs at specified intervals as provided by the user.

4. *Email Notification*:
   - Sends the log file as an email attachment.
   - Email body includes:
   - Starting time of scanning.
   - Total number of files scanned.
   - Total number of duplicate files found.

5. *Error Handling and Validation*:
   - Robust error handling for expected exceptions.
   - Validates inputs before performing any actions.

#### *Contact*

For any issues or queries, please contact:
- *Mahesh Dinkar Pawar*: maheshpawar30627@gmail.com

#### *Acknowledgment*

*Note*: Always ensure to perform a backup before running the script to avoid accidental data loss.
-----
This Readme.txt provides a comprehensive guide on how to use the DuplicateFileRemoval.py script, including its features, command-line options, 
and usage instructions.

----------------------------------------------------------------------------------------------------------------------
----------------------------------------Created By Mahesh Pawar-------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------