import os
import shutil

def move_py_files_to_hidden_folder(directory):
    # Create the hidden_folder inside the target_directory if it doesn't exist
    hidden_directory = os.path.join(directory, 'hidden_folder')
    os.makedirs(hidden_directory, exist_ok=True)

    # Move all .py files to the hidden_folder
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                new_path = os.path.join(hidden_directory, file)
                shutil.move(file_path, new_path)
                print(f"File moved to {new_path}")

if __name__ == "__main__":
    target_directory = "C:/Users/Hiwi/Desktop/dudududde/F"  # Specify the correct path for the target directory

    move_py_files_to_hidden_folder(target_directory)
