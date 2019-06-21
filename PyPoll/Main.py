import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

total_votes = []
all_candidate = []
percent_won = []
total_votes_won = []
pop_vote_won = []

with open (election_data, 'r') as csvfile:
csvreader = csv.reader(csvfile,delimiter=",")
header = next(csvreader)

