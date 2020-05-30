#The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

#Import the csv module. 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

print("successful run")