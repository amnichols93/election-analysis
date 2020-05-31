# 1) Import the csv and os modules 
import csv
import os

# 2) Assign a variable for the file to load and the path.
file_to_load = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "Resources", "election_results.csv")
# 3) Assign a variable for the file to save and the path.
file_to_save = os.path.join("C:\\Users", "amnic", "Desktop", "Berkeley", "3Election", "election-analysis", "analysis", "election_analysis.txt")

# 4) Initialize the variables, lists, and dictionaries
# 4.1) Total vote counter
total_votes = 0

# 4.2) Candidate variables, lists, and dictionaries
# 4.2.1) Candidate name list
candidate_options = []

# 4.2.2) Candidate dictionary to later count votes
candidate_votes = {}

# 4.2.3) Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 4.3) County variables, lists, and dictionaries
# 4.3.1) Total COUNTY vote counter
total_county_votes = 0

# 4.3.2) County name list
county_options = []

# 4.3.3) Candidate dictionary to later count votes
county_votes = {}

# 4.3.4) Winning County and Winning Count Tracker
winning_county_name = ""
winning_county_vote = 0
winning_county_percentage = 0

# 5) Read the .csv file to pull data
# 5.1) Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # 5.2) Read and skip the header row.
    headers = next(file_reader)

    # 5.3) Interate through each row in the CSV file
    for row in file_reader:
        
        # 5.3.1) Tally the total vote count
        total_votes += 1

        # 5.3.2) Tally the total county vote count
        total_county_votes += 1

        # 5.3.3) Identify the candidate name from each row
        candidate_name = row[2]
        
        # 5.3.4) Identify the county name from each row
        county_name = row[1]

        # 5.3.5) Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            # 5.3.5.1) Set initial candidate count to zero
            candidate_votes[candidate_name] = 0

        # 5.3.6) Tally each candidate's vote count
        candidate_votes[candidate_name] +=1

        # 5.3.7) Add the county name to the county list
        if county_name not in county_options:
            
            county_options.append(county_name)

            # 5.3.7.1) Set initial county count to zero
            county_votes[county_name] = 0

        # 5.3.8) Add a vote to the county's count
        county_votes[county_name] +=1


# 6) Write results to our text file
# 6.1) Open the text file with the ability to write to it
with open(file_to_save, "w") as txt_file:

# 6.2) Output the total vote count in the terminal and text file
    # 6.2.1) Print total vote count to terminal
    total_election_results = (
        f'\nElection Results\n'
        f'-----------------------\n'
        f"Total Votes: {total_votes:,}\n"
        f'-----------------------\n\n')
    print(total_election_results, end="")

    # 6.2.2) Write total vote count to the text file
    txt_file.write(total_election_results)

# 6.3) Output the COUNTY vote details to the terminal and text file
    # 6.3.1) Output section header "County Votes:" to text file.
    txt_file.write(f'County Votes:\n')

    # 6.3.2) Iterate through county list
    for county in county_votes:
        
        # 6.3.2.1) Retrieve vote count of a candidate
        countyvotes = county_votes[county]
        
        # 6.3.2.2) Calculate percentage of votes
        county_vote_percentage = float(countyvotes) / float(total_county_votes) * 100
        
        # 6.3.2.3) Determine candidate names with their percentage of votes
        county_results = (f'{county}: {county_vote_percentage:.1f}% {countyvotes:,}\n')

        # 6.3.2.4) Print the results to the terminal and write them to the text file
        print(county_results)
        txt_file.write(county_results)

        # 6.3.2.5) Determine the winning candidate and their vote details
        if (countyvotes > winning_county_vote) and (county_vote_percentage > winning_county_percentage):
            winning_county_vote = countyvotes
            winning_county_percentage = county_vote_percentage
            winning_county_name = county

    # 6.3.3) Establish the "winning county" text output
    winning_county_summary = (
        f"\n----------------------\n"
        f"Largest County Turnout: {winning_county_name}\n"
        f"----------------------\n")

    # 6.3.4) Write winning county summary to the text file and print to terminal
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

# 6.4) Output the CANDIDATE vote details to the terminal and text file
    # 6.4.1) Iterate through candidate list
    for candidate in candidate_votes:

        # 6.4.1.1) Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        
        # 6.4.1.2) Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # 6.4.1.3) Print candidate names with their percentage of votes.
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% {votes:,}\n')

        # 6.4.1.4) Print each candidate, their voter count, and percentage to the terminal and write it to the text file
        print(candidate_results)
        txt_file.write(candidate_results)

        # 6.4.1.5) Determine winning candidate and the vote details
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # 6.4.2) Establish the "winning candidate" text output
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")

    # 6.4.3) Print the winning candidate summary to the terminal and write it to the text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)