import os
import shutil

path = "/Users/navdeeptaliyan/Downloads"  # Use regular slashes for the path

try:
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_extension = os.path.splitext(file)[1].lower()
            # Create destination directory based on file extension
            dest_dir = os.path.join(path, file_extension[1:])
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # Move file to destination directory
            shutil.move(os.path.join(path, file), os.path.join(dest_dir, file))
    print("Files organized successfully!")
except Exception as e:
    print(f"An error occurred: {e}")

input("Press enter to exit!")  # Fixed the input message
