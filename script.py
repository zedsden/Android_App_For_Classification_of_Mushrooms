import os
import shutil

def move_files(source_folder="", destination_folder=""):
    # Iterate through all subdirectories in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            # Move the file to the destination folder
            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} to {destination_path}")

# Specify the main folders
main_folders = ['poisonous', 'edible', 'deadly', 'conditionally_edible']

# Specify the desired common folder name
common_folder = 'all_species_images'

# Iterate through each main folder and move files to the common folder
for folder in main_folders:
    source_folder = folder
    destination_folder = common_folder

    # Create the destination folder if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move files from all subdirectories to the common folder
    move_files(source_folder, destination_folder)