import os
import shutil
import time
import datetime
import sys
import select

# Initialize a list to store log messages
log_messages = []

# To control the infinite loop in the synchronize_folders function
boolean = True

''' 
    This function serves change the value of the boolean to False
    if the synchronization process is no longer needed.
'''
def check_for_q_input():

    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        char = sys.stdin.read(1)
        if char == "q":
            global boolean
            boolean = False

# Add a time stamp to each message
def log(message):

    time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_messages.append(f"{time} {message}")

'''
    The function that synchronize the main folder to the copy folder (one way synchronization). 
    It is possible to Create, Remove and Copy files between the Main folder to the Copy folder.
    
    Variables:
            main -> the path to the main folder
            copy -> the path to the copy folder
            log_file -> the path to the log txt
'''
def synchronize_folders(main, copy, log_file):
    while boolean:
        check_for_q_input()

        # Ensure main folder exists
        if not os.path.exists(main):
            print(f"Main folder '{main}' does not exist.")
            return

        # Ensure copy folder exists
        if not os.path.exists(copy):
            os.makedirs(copy)

        # Get lists of items (files and subfolders)
        main_items = set(os.listdir(main))
        copy_items = set(os.listdir(copy))

        # Items to be copied from main to copy
        items_to_copy = main_items - copy_items

        # Items to be removed from copy
        items_to_remove = copy_items - main_items

        # Synchronize items
        for item_to_copy in items_to_copy:

            main_item_path = os.path.join(main, item_to_copy)
            copy_item_path = os.path.join(copy, item_to_copy)

            # Copied files | print to the console and add to log
            if os.path.isfile(main_item_path):

                shutil.copy2(main_item_path, copy_item_path)
                print(f"Copied file: {main_item_path} -> {copy_item_path}")
                log(f"Copied file: {main_item_path} -> {copy_item_path}")

            # Creating folders | print to the console and add to log
            elif os.path.isdir(main_item_path):

                shutil.copytree(main_item_path, copy_item_path)
                print(f"Created folder: {copy_item_path}")
                log(f"Created folder: {copy_item_path}")

        # Remove items from copy that are not in source
        for item_to_remove in items_to_remove:

            copy_item_path = os.path.join(copy, item_to_remove)

            # Remove files | print to the console and add to log
            if os.path.isfile(copy_item_path):

                os.remove(copy_item_path)
                print(f"Removed file: {copy_item_path}")
                log(f"Removed file: {copy_item_path}")

            # Remove folders | print to the console and add to log
            elif os.path.isdir(copy_item_path):

                shutil.rmtree(copy_item_path)
                print(f"Removed folder: {copy_item_path}")
                log(f"Removed folder: {copy_item_path}")

        # add a message to the log_messages list
        with open(log_file, "w") as f:
            for message in log_messages:
                f.write(message + "\n")

        # Sleep for 1 second before checking again
        time.sleep(1)