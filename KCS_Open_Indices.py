"""
Make a walk thru C:\Alaris\TempImages
"""

import os

directory = r"C:\Alaris\TempImages"

list_of_KCP_jobs = []

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isdir(file_path):    # checking if is a directory
        list_of_KCP_jobs.append(file_path)

count_of_jobs = 1
for job in list_of_KCP_jobs:
    print("Job Number:", count_of_jobs, "Name:", job)
    count_of_jobs += 1


