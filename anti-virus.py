import os
import glob
import shutil

def move_py_files_to_hidden_folder(directory):
    # Create the hidden_folder inside the target_directory if it doesn't exist
    hidden_directory = os.path.join(directory, 'hidden_folder')
    os.makedirs(hidden_directory, exist_ok=True)

    # Move all .py files to the hidden_folder
    python_files = glob.glob(os.path.join(directory, '*.py'))
    for file in python_files:
        new_path = os.path.join(hidden_directory, os.path.basename(file))
        shutil.move(file, new_path)
        print(f"File moved to {new_path}")

def move_hidden_files_back(directory):
    # Specify the hidden_folder path
    hidden_directory = os.path.join(directory, 'hidden_folder')

    # Move all .py files from hidden_folder back to the target_directory
    hidden_files = glob.glob(os.path.join(hidden_directory, '*.py'))
    for file in hidden_files:
        new_path = os.path.join(directory, os.path.basename(file))
        shutil.move(file, new_path)
        print(f"File moved back to {new_path}")

if __name__ == "__main__":
    target_directory = "C:/Users/Hiwi/Desktop/dudududde/F"  # Specify the correct path for the target directory

    # Move .py files to hidden_folder
    move_py_files_to_hidden_folder(target_directory)

    # Move .py files from hidden_folder back to the target_directory
    move_hidden_files_back(target_directory)
