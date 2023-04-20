import os
import csv

election_data_path = os.path.join(os.path.dirname(__file__),'Resources', 'election_data.csv')

with open(election_data_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    header = next(csvreader)

    #initialize candidate dict. (tot votes, percent) and num rows
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
        #initialize dictionary with current candidate as key and 1 as vote count, 0 as percent
            candidate_dict[current_candidate] = [1,0]
        #add to the votes a candidate already has
        else:
            candidate_dict[current_candidate][0] += 1
        


#start finding the output string
output_string = f'''\
Election Results
-------------------------
Total Votes:  {num_votes}
-------------------------\
'''

#initialize the winner
winner = ""

for candidate in candidate_dict:
#find the percentages of the candidates' votes and store them in the dict    
    candidate_dict[candidate][1] = round(candidate_dict[candidate][0]*100/num_votes,3)
#add in each of the candidates with their names, total votes, and percentages
    output_string = "".join([output_string, 
    f"\n{candidate}: {candidate_dict[candidate][1]}% ({candidate_dict[candidate][0]})"])
    #find winner: start by assuming it's first person, then update as you go along
    if winner == "":
        winner = candidate
    #update winner if the current candidate has more votes
    elif candidate_dict[candidate][0] > candidate_dict[winner][0]:
        winner = candidate

#add in winner to output string
output_string += f'''\
\n-------------------------
Winner: {winner}
-------------------------
'''

#print output string
print(output_string)

#make path to the output .txt file
election_results_path = os.path.join(os.path.dirname(__file__), 'Election_Results.txt')

#output string to a file
with open(election_results_path,'w') as f:
    f.write(output_string)