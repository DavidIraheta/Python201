# Add the code for the file counter script that you wrote in the course.
# In the previous module of this course, you wrote a script that was able to move all your screenshots from your 
# messy desktop into a new folder. In this project, you'll revisit your file mover code and expand on it 
# with the knowledge of some additional data types in order to make it more flexible and powerful.
# When you built your file mover, you used the pathlib module that worked with Path() objects. 
# You can consider Path() objects as yet another data type, one that is more custom and not considered a built-in
# type. As you might remember, you'll have to import it from the standard library in order to work with it.
# In this project, you'll continue to work with pathlib and files, 
# but you'll also use some of the additional built-in data types that you got to know in this section.
from pathlib import Path

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
        
        # Move screenshots to the screenshot folder
        if "screenshot" in file.stem.lower():
            destination = screenshot_folder / file.name
            if destination.exists():  # Handle duplicate files by renaming
                destination = screenshot_folder / f"copy_of_{file.name}"
            file.rename(destination)

# Print the count of each file type
for ext, count in file_count.items():
    print(f"There are {count} file(s) with the '{ext}' extension on your desktop.")

# count = {'': 2, '.pdf': 2}
# file_out = open("file_count.txt", "w")
# file_out.write(str(count))
# file_out.close()
# # 'append' mode
# file_out = open("filecounts.txt", "a")
# file_out.write(str(count))
# file_out.write("\n")  # Include a line break
# file_out.close()
# file_in = file_out = open("filecounts.txt", "r")
# contents = file_in.read()
# print(contents)
# file_in.close()
# with open("filecounts.txt", "r") as file_in:
#     print(file_in.read())
import csv
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)


