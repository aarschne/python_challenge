import csv
import os

#declare the path to the csv of bank values
py_bank_csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(py_bank_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header and store it
    header = next(csvreader)

    #initialize variables
    sum_profit_losses = 0
    profit_losses = []
    current_profit_loss = 0

    # Loop through the csv data
    for row in csvreader:
        current_profit_loss = int(row[1])
        sum_profit_losses += current_profit_loss
        profit_losses.append([row[0],current_profit_loss])

    #Find number of months
    num_months = len(profit_losses)

    #initialize difference list
    differences = []

    #iterate over the profits and create a list of the differences
    for i in range(len(profit_losses)-1):
        differences.append([profit_losses[i+1][0], profit_losses[i+1][1]-profit_losses[i][1]])
    
    #initialize the sum of the differences and the extreme values
    sum_differences = 0
    max_diff = differences[0][1]
    month_max_diff = differences[0][0]
    min_diff = differences[0][1]
    month_min_diff = differences[0][0]

    #find the sum and the extreme values
    for diff in differences:
        sum_differences += diff[1]
        if diff[1] < min_diff:
            min_diff = diff[1]
            month_min_diff = diff[0]
        if diff[1] > max_diff:
            max_diff = diff[1]
            month_max_diff = diff[0]
    
    #find the average difference
    average_diff = sum_differences/len(differences)

#Create the output string    
output_string = f'''\
Financial Analysis
----------------------------
Total Months:  {num_months}
Total: ${sum_profit_losses}
Average Change: ${round(average_diff,2)}
Greatest Increase in Profits: {month_max_diff} (${max_diff})
Greatest Decrease in Profits: {month_min_diff} (${min_diff})\
'''

#print the output to the terminal
print(output_string)

#financial analysis path creation
analysis_path = os.path.join(os.path.dirname(__file__), 'Financial_analysis.txt')

#output the string to a text file
with open(analysis_path, 'w') as f:
    f.write(output_string)