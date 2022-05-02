"""
Make a list of all the open indices inside the Temporal Directory
Normally the jobs are in C:\ScanPro
I have it in C:\Alaris\TempImages
"""


import os

# Ask the user for the Temp path 
user_input = input("Please write the Temporal Directory or hit Enter for default: ")

if user_input == "":
    temp_jobs_directory = r"C:\Alaris\TempImages"
else:
    if os.path.isdir(user_input):
        temp_jobs_directory = user_input
    else:
        print("Please write a valid path")
        exit()


# Walk thru the Temporal Jobs Directory
with open("C:\Temp\open_indices", "w") as open_indices_handle:      # Open file and erase old content
    for base_path, directories, files in os.walk(temp_jobs_directory):
        for file_name in files:
            if file_name == "index":
                # Get the relative path extracting the base path and "\"
                relative_path = base_path.replace(temp_jobs_directory + "\\", "")
                path_parts = relative_path.split(os.sep)

                # If it's a document level index
                if len(path_parts) == 3: 
                    document_index_path = os.path.join(base_path, file_name)
                    job =      path_parts[0]
                    batch =    path_parts[1]
                    document = path_parts[2]
                    # Read the current index data
                    with open(document_index_path) as document_index_handle:
                        # Read the index data but the header ([____Default____]) and the last newline (\n)  
                        index_data = document_index_handle.readlines()[1:-1]    
                        print(index_data)
                        header = job + batch + document
                        open_indices_handle.write(header)
                        open_indices_handle.writelines(index_data)  # Don't write the last newline
                





   

