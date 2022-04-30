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
    print("Job Number", count_of_jobs+1, "Name:", job)
    count_of_jobs += 1


# Ask the user for a job to scan
prompt = "Please select a job number or Enter to exit (1 - " + str(count_of_jobs) + "): "
while True:
    user_input = input(prompt)
    if user_input == "":
        exit()
    if user_input.isdigit() and (1 <= int(user_input) <= count_of_jobs):
        break

selected_job_number = int(user_input)

job_directory = os.path.join(job_directory, list_of_KCP_jobs[selected_job_number-1])

list_of_batches = list_of_directories(job_directory)
print("job_directory:", job_directory) # !!!

print("\nThere are ", len(list_of_batches), " batches in \"", \
    list_of_KCP_jobs[selected_job_number-1], "\"\n", sep="")


count_of_batches = 0
for batch in list_of_batches:
    print("Batch Number", count_of_batches+1, "Name:", batch)
    count_of_batches += 1

prompt = "Please select a batch number to scan or Enter to exit (1 - " + str(count_of_batches) + "): "

while True:
    user_input = input(prompt)
    if user_input == "":
        exit()
    if user_input.isdigit() and (1 <= int(user_input) <= count_of_batches):
        break

selected_batch_number = int(user_input)

batch_directory = os.path.join(job_directory, list_of_batches[selected_batch_number-1])

print("batch_directory:", batch_directory)

list_of_documents = list_of_directories(batch_directory)

print("list_of_documents:", list_of_documents)


for document in list_of_documents:
    document_directory = os.path.join(batch_directory, document)
    list_of_images = list_of_directories(document_directory)
    
    for image in list_of_images:
        index_filename = os.path.join(document_directory, "index")
        print("index_filename", index_filename)

