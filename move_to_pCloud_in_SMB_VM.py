import shutil
import os
import time

def move_files_and_folders(src_folder_path, dest_folder_path, file_states):
    """
    Moves new or updated files and folders from the source folder to the destination folder.
    Tracks the state of files to identify new or modified files.
    """
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    for item in os.listdir(src_folder_path):
        src_item = os.path.join(src_folder_path, item)
        dest_item = os.path.join(dest_folder_path, item)

        if os.path.isdir(src_item) or os.path.isfile(src_item):
            src_mtime = os.stat(src_item).st_mtime

            if src_item not in file_states or file_states[src_item] < src_mtime:
                shutil.move(src_item, dest_item)
                file_states[src_item] = src_mtime
                print(f"Item '{src_item}' has been moved to '{dest_item}'")

def monitor_and_move_loop(src_folder, dest_folder):
    """
    Continuously monitors the source folder for new or updated files and moves them to the destination folder.
    """
    file_states = {}

    while True:
        move_files_and_folders(src_folder, dest_folder, file_states)
        time.sleep(1)  # Wait for 1 second before checking again

# Example Usage
source_folder = "/path_of_SMB_share"
destination_folder = "/path_of_home/pCloudDrive/share"

monitor_and_move_loop(source_folder, destination_folder)

#run this as a service