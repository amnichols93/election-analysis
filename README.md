# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election. 

1. Determine the total number of votes cast.
2. Determine a complete list of candidates who received votes.
3. Determine the percentage of votes each candidate won.
4. Determine the total number of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.3, Visual Studio Code 1.45.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85213 number of votes. 
  - Diana DeGette received 73.8% of the vote and 272892 number of votes. 
  - Raymon Anthony Doane received 3.1% of the vote and 11606 number of votes. 
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272892 number of votes.
  
## Challenge Overview
The challenge was to use Python to write code that would read and analyze the "election_results.csv" file to determine the total number of votes cast, which candidates received votes, how many votes each candidate received and their percentage of the total, and who won. From there, the challege was to write those results to a separate text file that would act as a summary for whoever reviews the results.

## Challenge Summary
The code breaks down into the following structure:
  - Import the 'csv' and 'os' modules.
  - Identify the path to the .csv file we are reading, and the .txt file to which we are writing.
  - Initialize the variables that will ultimately be amended during the analysis.
  - Read the .csv file for the following tasks:
    - Skip the headers.
    - Use a "for" loop to:
      - Tally the total number of votes.
      - Identify the candidates for each ballot.
    - Use an "if, not in" statement to identify the candidates who received at least one vote.
    - Tally the number of votes each candidate received.
  - Write to the .txt file the following information:
    - A header titled "Election Results."
    - The total number of votes cast.
    - The number and percentage of votes for each candidate.
    - The name, number of votes, and percentage of votes for the winner.
