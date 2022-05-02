"""
Write the file "C:\Temp\all_open_indices.csv" with all the open indices inside the Temporal Directory
Reset the file "C:\Temp\all_open_indices.csv" every time the scrip runs
Normally the jobs are in "C:\ScanPro"
I have it in "C:\Alaris\TempImages"
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

document_counter = 0
# Open file and erase old content
with open(r"C:\Temp\all_open_indices.csv", "w") as open_indices_handle:
    # Write file header and newline
    open_indices_handle.write("Job Name, Batch Name, Document Number, Indices\n")
    
    # Walk thru the Temporal Jobs Directory      
    for base_path, directories, files in os.walk(temp_jobs_directory):
        for file_name in files:
            if file_name == "index":    # Only when the filename is "index"...
                # Get the relative path extracting the base path and "\"
                relative_path = base_path.replace(temp_jobs_directory + "\\", "")
                path_parts = relative_path.split(os.sep)

                # And if it's a document level index
                if len(path_parts) == 3: 
                    document_index_path = os.path.join(base_path, file_name)
                    job =      path_parts[0]
                    batch =    path_parts[1]
                    document = path_parts[2]
                    # Read the current index data
                    with open(document_index_path) as document_index_handle:
                        # Read the index data 
                        # except the file header ([____Default____]) and the last newline (\n)  
                        index_data = document_index_handle.readlines()[1:-1]    
                        
                        # Write index data to file, separated by commas
                        header = job + "," + batch + ","  + document + "," 
                        open_indices_handle.write(header)
                        open_indices_handle.writelines(index_data)
                    document_counter +=1

print(document_counter, "documents found.\n")

                