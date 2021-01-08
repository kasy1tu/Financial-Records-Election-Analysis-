#Import modules and created path to csv file 
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")

#Defined all variables 
total_count = 0 
unique_candidate = []
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0 
votes = []
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
totals = zip(candidate_list, votes)

#Open csv file as read 
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
#Looped through to identify unique candidates and store it in a list
    for row in reader:
        if row[2] not in unique_candidate: 
            unique_candidate.append(row[2])
#Count votes for each unique candidate and store it in a list
        total_count += 1
        if row[2] == "Khan":
            khan_votes += 1
        if row[2] == "Correy":
            correy_votes += 1
        if row[2] == "Li":
            li_votes += 1
        if row[2] == "O'Tooley":
            tooley_votes += 1
    votes.append(khan_votes)
    votes.append(correy_votes)
    votes.append(li_votes)
    votes.append(tooley_votes)
    for candidate_list in totals:
        if candidate_list[1] == max(votes):
            winner = candidate_list[0]

            #Find average vote count for each candidate 
khan = round((khan_votes)/(total_count), 2)
correy = round((correy_votes)/(total_count), 2)
li = round((li_votes)/(total_count), 2)
tooley = round((tooley_votes)/(total_count), 2)
li_times = round((li)*100, 2)

print("Election Results")
print("----------------------------------------------------------------")
print(f"Total Votes: {total_count}")
print(f"List of candidates: {unique_candidate}")
print("----------------------------------------------------------------")
print(f"Khan Total Votes: {khan_votes} | Percentage: {khan*100}%")
print(f"Correy Total Votes: {correy_votes} | Percentage: {correy*100}%")
print(f"Li Total Votes: {li_votes} | Percentage: {li_times}%")
print(f"O'Tooley Total Votes: {tooley_votes} | Percentage: {tooley*100}%")
print("----------------------------------------------------------------")
print(f"Winner: {winner}")