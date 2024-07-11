import sys
import time
import schedule
from Duplicate_Removal_Module import *

def main():
    print("------------------------------------------------------------------------")
    print("---------------------Created By Mahesh Pawar----------------------------")
    print("------------------------------------------------------------------------")
    print("\nApplication name : "+sys.argv[0],"\n")
    print("------------------------------------------------------------------------")

    if len(sys.argv) != 4:
        print("Usage: python DublicateFileRemoval.py <directory> <interval> <email>")
        sys.exit(1)

    directory = sys.argv[1]
    interval = sys.argv[2]
    email = sys.argv[3]

    try:
        validate_directory(directory)
        validate_interval(interval)
        validate_email(email)
        print(email,"this email verified successfully..\n")
        print(f"this task execute again after {interval} minute for deleting dublicate file from",directory,"\n")
        print("------------------------------------------------------------------------")

        interval_minutes = int(interval)
        
        schedule.every(interval_minutes).minutes.do(Main_Task, directory, email,interval)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
