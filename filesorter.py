import os
import shutil

print("file sorter")

# path from the directory you want to sort

# TYPE IN YOUR PATH YOU WANT TO SORT
path = ""

file_list = []
all_file_types = []
file_types = []

# list all files
for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):
        file_list.append(filename)

# print out all files in the directory
print(file_list)

# find all endings after the . which contains the informations which datatype the file is and saves all endings in an array
for ending in file_list:
    all_file_types.append(ending.split(".")[-1])

# all_file_types contains all endings, but we want it without duplicates. this is the problem we are solving right here
file_types = list(set(all_file_types))

# loop over all file types (no duplicates)
for i in file_types:

    # make a new folder for every file ending in file types and name the folder like the ending
    new_folder_path = os.path.join(path, i)
    os.makedirs(new_folder_path,exist_ok=True)

    # make a temporary array where all files with the same ending been saved
    sorted_files = [file for file in file_list if file.endswith(f".{i}")]

    # loop over the sorted_files where all files have the same ending
    for file in sorted_files:

        # define a source_path, where the files are now
        source_path = os.path.join(path,file)
        
        # define a destination_path where the files are moved to
        destination_path = os.path.join(path, i)
        
        # move the files from source to destination
        shutil.move(source_path, destination_path)
    print("All files moved successfully!")




