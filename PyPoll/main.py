import os
import csv
election_data_csv =os.path.join('Resources', "election_data.csv")
Election_Analysis = os.path.join("Analysis", "PyPoll_Analysis.txt")

voter_id = []
candidate_list = []
candidate_votes = []
votes_per_candidate = {}
voting_results = {}
percentages = []


# List Construction
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        #Determing amount of voter ids
       voter_id.append(row[0])
       candidate_votes.append(row[2]) 
       #Candidate List
       if row[2] not in candidate_list:
           candidate_list.append(row[2])

for value in candidate_votes:
    if value in voting_results.keys():
        voting_results[value] += 1
    else:
        voting_results[value] = 1
        
# Determining Winner
winner = [key for key, value in voting_results.items() if value == max(voting_results.values())]

for value in candidate_votes:
    if value in voting_results.keys():
        voting_results[value] += 1
    else:
        voting_results[value] = 1
    
# Determining Winner
winner = [key for key, value in voting_results.items() if value == max(voting_results.values())]

# Printing 
print(f"Total Votes: {len(voter_id)}")
print("---------- ")
for i in voting_results:
    print(i, voting_results[i])
    print(f"{((voting_results[i])/(len(voter_id)))*100}%")
    print("-----")
print(f" Winner: {winner}")

#Text File Creation
f = open(Election_Analysis, "w")
print((f"Total Votes: {len(voter_id)}"), file=f)
print(("---------- "), file=f)
for i in voting_results:
    print((i, voting_results[i]), file=f)
    print((f"{((voting_results[i])/(len(voter_id)))*100}%"), file=f)
    print(("-----"), file=f)
print((f" Winner: {winner}"), file=f)
f.close