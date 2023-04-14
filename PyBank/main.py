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
    num_months = 0
    profit_losses = []
    current_profit_loss = 0

    # Loop through the csv data
    for row in csvreader:
        current_profit_loss = int(row[1])
        sum_profit_losses += current_profit_loss
        num_months += 1
        profit_losses.append(current_profit_loss)

    #initialize difference list
    differences = []

    #iterate over the profits and create a list of the differences
    for i in range(len(profit_losses)-1):
        differences.append(profit_losses[i+1]-profit_losses[i])
    
    #initialize the sum of the differences to find the average
    sum_differences = 0

    #find the sum
    for diff in differences:
        sum_differences += diff
    
    #find the average difference
    average_diff = sum_differences/len(differences)
    
    #print statments to test the correctness of the values
    print(round(average_diff,2))
    print(num_months)
    print(sum_profit_losses)
    
