# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.
from pathlib import Path
import csv
# Dictionary to count file types
file_count = {}

# Define paths
desktop = Path.home() / "Desktop"
screenshot_folder = desktop / "untitled folder"
screenshot_folder.mkdir(exist_ok=True)  # Create Screenshots folder if it doesn't exist

# Loop through each file on the desktop
for file in desktop.iterdir():
    if file.is_file():  # Only process files, not directories
        file_extension = file.suffix.lower()
        
        # Update file count dictionary
        file_count[file_extension] = file_count.get(file_extension, 0) + 1
        
        # Move screenshots to the screenshot folder spaghetti
        if "screenshot" in file.stem.lower():
            destination = screenshot_folder / file.name
            if destination.exists():  # Handle duplicate files by renaming
                destination = screenshot_folder / f"copy_of_{file.name}"
            file.rename(destination)

csv_path = desktop / "file_count.csv"

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Extension", "Count"])
    for ext, count in file_count.items():
        writer.writerow([ext, count])
        
for ext, count in file_count.items():
    print(f"There are {count} file(s) with the '{ext}' extension on your desktop.")