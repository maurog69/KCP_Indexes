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


# Make a list of the directories below 
list_of_KCP_jobs = []

for filename in os.listdir(temp_kcp_directory):
    file_path = os.path.join(temp_kcp_directory, filename)
    
    if os.path.isdir(file_path):    # checking if is a directory
        list_of_KCP_jobs.append(filename)

count_of_jobs = 1
for job in list_of_KCP_jobs:
    print("These are the available jobs:") 
    print("Job Number:", count_of_jobs, "Name:", job)
    count_of_jobs += 1


