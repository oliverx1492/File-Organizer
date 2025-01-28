# FileSorter - A Simple File Organizer

## About the Project
FileSorter is a Python script designed to help you organize your files efficiently. It scans a specified directory, identifies files by their formats, creates a folder for each file type, and moves the files into their respective folders.

For example:
- All `.pdf` files will be moved into a folder named `pdf`.
- All `.jpg` files will be moved into a folder named `jpg`.

This tool is perfect for decluttering your working space and keeping files organized.

---

## How to Use

### Step 1: Install Python
If you haven't already, install Python on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Modify the Script
1. Open the `filesorter.py` script in any code editor (e.g., VS Code).
2. Locate the `path` variable (around line 9).
3. Set the `path` variable to the directory you want to organize. Use the following format for the path:
   ```python
   path = "C:/Your/path/to/directory"

### Step 3: Run the Script
1. Open your command line (e.g., Command Prompt on Windows, Terminal on macOS/Linux)
2. Navigate to the directory where filesorter.py is located using the cd command "cd path/to/your/script"
3. Run the script with following command: "python filesorter.py"

Your files will now be sorted into folders based on their file types. Enjoy your organized workspace!


