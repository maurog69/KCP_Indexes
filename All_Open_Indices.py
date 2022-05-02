"""
Make a list of all the open indices inside the Temporal Directory
Normally the jobs are in C:\ScanPro
I have it in C:\Alaris\TempImages
"""


import os


user_input = input("Please write the Temporal Directory or hit Enter for default: ")

if user_input == "":
    temp_jobs_directory = r"C:\Alaris\TempImages"
else:
    if os.path.isdir(user_input):
        temp_jobs_directory = user_input
    else:
        print("Please write a valid path")
        exit()


for base_path, directories, files in os.walk(temp_jobs_directory):
   for name in files:
       if name == "index":
           # Get the relative path extracting the base path and "\"
           relative_path = base_path.replace(temp_jobs_directory + "\\", "")
           path_parts = relative_path.split(os.sep)

           # If it's a document level index
           if len(path_parts) == 3: 
               print(os.path.join(base_path, name))
   

