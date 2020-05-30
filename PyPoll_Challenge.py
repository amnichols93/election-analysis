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

#Initialize a total county vote counter.
total_county_votes = 0

#Initialize county name list
county_options = []

#Initialize candidate dictionary to later count votes
county_votes = {}

# Winning County and Winning Count Tracker
winning_county_name = ""
winning_county_vote = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        # Add to to the total vote count
        total_votes += 1

        # Add to to the total county vote count
        total_county_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
        
        #Print the county name from each row
        county_name = row[1]

        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            #Track votes per candidate
            ## Set them all to zero
            candidate_votes[candidate_name] = 0

        #Add a vote to the candidate's count
        candidate_votes[candidate_name] +=1

        #Add the county name to the county list
        if county_name not in county_options:
            
            county_options.append(county_name)

            #Track votes per county
            ## Set them all to zero
            county_votes[county_name] = 0

        #Add a vote to the county's count
        county_votes[county_name] +=1
    
#Save results to our text file
with open(file_to_save, "w") as txt_file:

    #Print final vote count to terminal
    ### Election Results
    ### ------------------
    ### Total Votes: (Number)
    ### ------------------
    ### (Line Break)
    total_election_results = (
        f'\nElection Results\n'
        f'-----------------------\n'
        f"Total Votes: {total_votes:,}\n"
        f'-----------------------\n\n')
    print(total_election_results, end="")
    #Save final vote count to the text file.
    txt_file.write(total_election_results)

    ### County Votes:
    txt_file.write(f'County Votes:\n')
###
    #Iterate through candidate list
    for county in county_votes:
        #Retrieve vote count of a candidate
        countyvotes = county_votes[county]
        #Calculate percentage of votes
        county_vote_percentage = float(countyvotes) / float(total_county_votes) * 100
        #Print candidate names with their percentage of votes.
        county_results = (f'{county}: {county_vote_percentage:.1f}% {countyvotes:,}\n')

        #Save the results to the text file.
        txt_file.write(county_results)

        #Determine winning candidate and the vote details
        if (countyvotes > winning_county_vote) and (county_vote_percentage > winning_county_percentage):
            winning_county_vote = countyvotes
            winning_county_percentage = county_vote_percentage
            winning_county_name = county

    winning_county_summary = (
        f"\n----------------------\n"
        f"Largest County Turnout: {winning_county_name}\n"
        f"----------------------\n")

    #Write winning candidate summary to the text file
    txt_file.write(winning_county_summary)

###


    #Iterate through candidate list
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print candidate names with their percentage of votes.
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% {votes:,}\n')

        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #Save the results to the text file.
        txt_file.write(candidate_results)

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
    #Write winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)

print("End of successful run.")