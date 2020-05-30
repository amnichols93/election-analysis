#The data we need to retrieve. 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

#Import the csv and os modules 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Initialize candidate name list
candidate_options = []

#Initialize candidate dictionary to later count votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        # Add to to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            #Track votes per candidate
            ## Set them all to zero
            candidate_votes[candidate_name] = 0

        ##Add a vote to the candidate's count
        candidate_votes[candidate_name] +=1

print(f'The total number of votes cast is {total_votes}.')
print(f'The candidates are {candidate_options}.')
print(f'The votes for each candidate are {candidate_votes}.')

#Iterate through candidate list
for candidate in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    #Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #Print candidate names with their percentage of votes.
    print(f'{candidate}: {vote_percentage:.1f}% {votes:,}')

    #Determine winning candidate and the vote details
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

winning_candidate_summary = (
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n")

print(winning_candidate_summary)

print("End of successful run.")