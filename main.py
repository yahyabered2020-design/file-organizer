import os
import shutil

path = r"C:\Users\yahya hassan\OneDrive\Documents\Web Development Projects\file-organizer\test_folder"

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    extension = extension.lower()

    if extension in [".jpg", ".png"]:
        folder = "Images"

    elif extension in [".pdf", ".docx", ".txt"]:
        folder = "Documents"

    elif extension in [".mp4", ".mov"]:
        folder = "Videos"

    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(
        os.path.join(path, file),
        os.path.join(folder_path, file)
    )

print("Files organized successfully!")