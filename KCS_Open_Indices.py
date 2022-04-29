"""
Make a list of jobs inside the Temporal Directory
Normally is C:\ScanPro
I have it in C:\Alaris\TempImages
"""

import os


def list_of_directories(path):
    """
    Returns a list of the directories below "path"
    """
    list_of_directories = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
    
        if os.path.isdir(file_path):    # checking if is a directory
            list_of_directories.append(filename)
    return list_of_directories




user_input = input("Please write the Temporal Directory or hit Enter for default: ")

if user_input == "":
    job_directory = r"C:\Alaris\TempImages"
else:
    if os.path.isdir(user_input):
        job_directory = user_input
    else:
        print("Please write a valid path")
        exit()



list_of_KCP_jobs = list_of_directories(job_directory)
print("These are the available jobs:") 

count_of_jobs = 0
for job in list_of_KCP_jobs:
    print("Job Number:", count_of_jobs+1, "Name:", job)
    count_of_jobs += 1


# Ask the user for a job to scan
prompt = "Please select a job number or enter to exit (1 - " + str(count_of_jobs) + "): "
while True:
    user_input = input(prompt)
    if user_input == "":
        exit()
    if user_input.isdigit() and (1 <= int(user_input) <= count_of_jobs):
        break

selected_job_number = int(user_input)

job_directory = os.path.join(job_directory, list_of_KCP_jobs[selected_job_number-1])

list_of_batches = list_of_directories(job_directory)
print("job_directory:", job_directory)

print("\nYou have selected job ", user_input, ", \"", list_of_KCP_jobs[selected_job_number-1], \
    "\", with ", len(list_of_batches), " batches.\n", sep="")

for batch in list_of_batches:
    list_of_documents = list_of_directories(os.path.join(job_directory, batch))
    print("list_of_documents", list_of_documents, "in batch", batch)

