"""
Write the file "C:\Temp\open_indices.csv" with the selected job open indices
inside the Temporal Directory of Kodak Capture Pro.
Reset the file "C:\Temp\open_indices.csv" every time the scrip runs.
By default the jobs are in "C:\ScanPro".
I have it in "C:\Alaris\TempImages"
"""

import os


def list_of_directories(path):
    """
    This function returns a list of the directories below "path"
    """
    # List comprehension 
    return [file.name for file in os.scandir(path) if file.is_dir()]



# Ask the user for the Temp path 
user_input = input("Please write the Temporal Directory or hit Enter for default: ")

if user_input == "":
    job_directory = r"C:\Alaris\TempImages"
else:
    if os.path.isdir(user_input):
        job_directory = user_input
    else:
        print("Please write a valid path")
        exit()



list_of_jobs = list_of_directories(job_directory)
print("These are the available jobs:") 

for count_of_jobs, job in enumerate(list_of_jobs):
    print("Job Number", count_of_jobs+1, "Name:", job)


# Ask the user for a job to scan
prompt = "Please select a job number or Enter to exit (1 - " + str(count_of_jobs + 1) + "): "
while True:
    user_input = input(prompt)
    if user_input == "":
        exit()
    if user_input.isdigit() and (1 <= int(user_input) <= count_of_jobs + 1):
        break

selected_job = list_of_jobs[int(user_input)-1]

job_directory = os.path.join(job_directory, selected_job)

list_of_batches = list_of_directories(job_directory)

print("\nThere are ", len(list_of_batches), " batches in \"", \
    selected_job, "\"\n", sep="")


# Ask the user for a batch to scan
for count_of_batches, batch in enumerate(list_of_batches):
    print("Batch Number", count_of_batches+1, "Name:", batch)


prompt = "Please select a batch number to scan or Enter to exit (1 - " + str(count_of_batches + 1) + "): "

while True:
    user_input = input(prompt)
    if user_input == "":
        exit()
    if user_input.isdigit() and (1 <= int(user_input) <= count_of_batches + 1):
        break


selected_batch = list_of_batches[int(user_input)-1]

batch_directory = os.path.join(job_directory, selected_batch)

list_of_documents = list_of_directories(batch_directory)


# Open file and erase old content
with open(r"C:\Temp\open_indices.csv", "w") as open_indices_handle:
    # Write file header and newline
    job_file_header = "Job Name: " + selected_job + "\n"
    open_indices_handle.write(job_file_header)

    batch_file_header = "Batch Name: " + selected_batch + "\n"
    open_indices_handle.write(batch_file_header)

    document_counter = 0
    for document in list_of_documents:
        document_directory = os.path.join(batch_directory, document)
        list_of_documents = list_of_directories(document_directory)
    
        index_filename = os.path.join(document_directory, "index")
        
        with open(index_filename) as document_index_handle:
            # Read the index data
            # except the file header ([____Default____]) and the last newline (\n)
            index_data = document_index_handle.readlines()[1:-1]    
            header = "Indices in document " + document + ": "
            open_indices_handle.write(header)
            open_indices_handle.writelines(index_data)

        document_counter += 1

print("\n", document_counter, "documents found.\n")

        

