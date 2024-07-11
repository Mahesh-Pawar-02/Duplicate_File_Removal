import os
import hashlib
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def hashfile(Path, blocksize = 1024):
    fd = open(Path,"rb")
    hasher = hashlib.md5()
    buffer = fd.read(blocksize)

    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()

def Delete_Files(files):
    try:
        for file in files:
            os.remove(file)
            print(f"Deleted duplicate file: {file}")
    except Exception as e:
        print(f"Error deleting file {file}: {str(e)}")

def Mail_Sender(log_file, email_id, stats):
    try:
        msg = MIMEMultipart()
        msg['From'] = "try.web.new@gmail.com"
        msg['To'] = email_id
        msg['Subject'] = "Duplicate Files Removal Log"

        body = f"""\
        <html>
        <body style="font-family: Verdana, sans-serif; color: blue; font-size: large;">
    <p>Hello..!</p>

    <p>Greeting from Mahesh Pawar.</p>
    <p>Please find the attached document which contains Log of Deleted Dublicate file.</p>
    
    <B style = "color:black;">Starting time of scanning: {stats['start_time']}</B><br>
    <B style = "color:black;">Total number of files scanned: {stats['files_scanned']}</B><br>
    <B style = "color:black;">Total number of duplicate files found: {stats['duplicates_found']}</B><br>

    <p>NOTE : This is auto generated mail.<p>

    <p>Thanks and Regards,</p>

    </p>
    Mahesh Dinkar Pawar<br>
    RID : PM0100047<br>
    +91 9322150275
    </p>
    </body>
    </html>
    """
        msg.attach(MIMEText(body, 'html'))

        with open(log_file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(log_file)}")
        msg.attach(part)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("try.web.new@gmail.com",  "qvbp xnrv pbcb ****")
            server.sendmail("try.web.new@gmail.com", email_id, msg.as_string())
            print("Log file successfully sent to :",email_id)
    except Exception as e:
        print(f"Error sending email to {email_id}: {str(e)}")

def validate_directory(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")

def validate_email(email):
    if "@" not in email or "." not in email.split("@")[1]:
        raise ValueError(f"Invalid email address: {email}")

def validate_interval(interval):
    if not interval.isdigit() or int(interval) <= 0:
        raise ValueError(f"Invalid interval: {interval}")


def Main_Task(directory, email_id,interval):
    
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Scanning started at: {start_time}")
    try:
        all_files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files]
        duplicates = Find_Duplicates(directory)
        Delete_Files(duplicates)
        
        end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Scanning ended at: {end_time}")
        
        stats = {
            "start_time": start_time,
            "end_time": end_time,
            "files_scanned": len(all_files),
            "duplicates_found": len(duplicates)
        }
        
        print(f"Total files scanned: {stats['files_scanned']}")
        print(f"Total duplicate files found: {stats['duplicates_found']}")
        ProcessLog()
        log_file = "Log/DuplicateFile.log"
        Log_File(log_file, stats,duplicates)
        Mail_Sender(log_file, email_id, stats)

    except Exception as e:
        print(f"Error in main_task: {str(e)}")

def Find_Duplicates(directory):
    try:
        checksums = {}
        duplicates = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                checksum = hashfile(file_path)
                if checksum in checksums:
                    duplicates.append(file_path)
                else:
                    checksums[checksum] = file_path
        return duplicates
    except Exception as e:
        print(f"Error finding duplicates in {directory}: {str(e)}")
        return []

def Log_File(file_path, stats,dublicates = []):
    try:
        with open(file_path, 'w') as f:
            separator = "_"*80

            f.write(separator + "\n")
            f.write("Welcome..! to Log File "+"\n")
            f.write("Log File created at : "+time.ctime()+"\n")
            f.write(separator + "\n")
            f.write("Duplicate File Removal Operation : \n")
            f.write(separator + "\n")

            for element in dublicates: 
                f.write("%s\n" % element)
            f.write("="*80 + "\n")
            f.write(f"Starting time of scanning: {stats['start_time']}\n")
            f.write(f"Ending time of scanning: {stats['end_time']}\n")
            f.write(f"Total number of files scanned: {stats['files_scanned']}\n")
            f.write(f"Total number of duplicate files found: {stats['duplicates_found']}\n")
           
    except Exception as e:
        print(f"Error writing stats to file: {str(e)}")

def ProcessLog(log_dir="Marvellous"):
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    log_path = os.path.join(log_dir, "DuplicateFile.log")

    print("Log File is successfully generated at location:", log_path)