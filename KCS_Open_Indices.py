"""
Make a list of jobs inside the Temporal Directory
Normally is C:\ScanPro
I have it in C:\Alaris\TempImages
"""

import os

user_input = input("Please write the Temporal Directory or hit Enter for default: ")

if user_input == "":
    temp_kcp_directory = r"C:\Alaris\TempImages"
else:
    if os.path.isdir(user_input):
        temp_kcp_directory = user_input
    else:
        print("Please write a valid path")
        exit()


# Make a list of the directories below "temp_kcp_directory"
list_of_KCP_jobs = []
for filename in os.listdir(temp_kcp_directory):
    file_path = os.path.join(temp_kcp_directory, filename)
    
    if os.path.isdir(file_path):    # checking if is a directory
        list_of_KCP_jobs.append(filename)

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
    if user_input.isdigit():
        break

selected_job_number = int(user_input)
print("You have selected job ", user_input, " ", list_of_KCP_jobs[selected_job_number])


