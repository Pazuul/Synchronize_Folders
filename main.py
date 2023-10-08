import argparse
from synchronize import synchronize_folders

if __name__ == "__main__":
    # arguments main, copy and log
    parser = argparse.ArgumentParser(description="Synchronize folders")
    parser.add_argument("--main", help="Path to the main folder")
    parser.add_argument("--copy", help="Path to the copy folder")
    parser.add_argument("--log", help="Path to the log file")
    args = parser.parse_args()
    main_folder = args.main
    copy_main = args.copy
    # At the end of the path please use a .txt file to log everything
    log_file = args.log
    # If some argument is not given the program will ask you for the input
    if main_folder is None or copy_main is None or log_file is None:
        print("Something went wrong when the arguments were give, please verify your input and try again.")
        print(f"--main = {main_folder} ; --copy = {copy_main} ; --log = {log_file}")
        exit(1)
    print("Starting Synchronization - To quit please input q on the terminal")
    # Enters in the synchronize process
    synchronize_folders(main_folder, copy_main, log_file)
    print("Synchronization completed. Log file created at:", log_file)