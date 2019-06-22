#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

#path
election_data = os.path.join("election_data.csv")

total_votes = 0
winner_vote = 0
total_candidate = 0
total_votes_won = ["", 0]
candidate_choice = []
pop_vote_won = {}

#open and read
with open("election_data.csv","r") as csvfile:

    reader = csv.reader(csvfile)
    for row in reader:
        #print(row)
        header = next(reader)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candiadate"]

        if row["Candiadate"] not in candidate_choice:

            candidate_choice.append(row["Candidate"])

            pop_vote_won[row["Candidate"]] = 1

        else:
            pop_vote_won[row["Candidate"]] = pop_vote_won[row["Candidate"]] + 1

print ("Election Results")
print ("----------------------")
print ("Total Votes " + str(total_votes))