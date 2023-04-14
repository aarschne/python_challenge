import os
import csv

election_data_path = os.path.join(os.path.dirname(__file__),'Resources', 'election_data.csv')

with open(election_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    header = next(csvreader)

    #initialize candidate list and num rows
    candidate_dict = {}
    num_votes = 0

    #loop through the rows of the csv file
    for row in csvreader:
        #find number of votes
        num_votes += 1

        #store the current candidate
        current_candidate = row[2]

        #try to find if the current candidate is in dictionary. If not, add them
        if current_candidate not in candidate_dict:
            candidate_dict[current_candidate] = [1,0]
        #add to the votes a candidate already has
        else:
            candidate_dict[current_candidate][0] += 1
        
#find the percentages of the candidates' votes and store them in the dict
for candidate in candidate_dict:
    candidate_dict[candidate][1] = round(candidate_dict[candidate][0]*100/num_votes,3)

#start finding the output string
output_string = f'''\
Election Results
-------------------------
Total Votes:  {num_votes}
-------------------------\
'''

for candidate in candidate_dict:
    output_string = "".join([output_string, 
    f"\n{candidate}: {candidate_dict[candidate][1]}% ({candidate_dict[candidate][0]})"])

output_string += "\n-------------------------"

print(output_string)