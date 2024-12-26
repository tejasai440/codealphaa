import os
import shutil
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".html", ".css", ".js"],
    "Others": [],
}

def organize_files(directory):
    """Organize files in the specified directory into categorized folders."""
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    for category in file_types.keys():
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, category))
                print(f"Moved: {file_name} -> {category}")
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others"))
            print(f"Moved: {file_name} -> Others")

    print("File organization complete.")
if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ").strip()
    organize_files(target_directory)


