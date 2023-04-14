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
        profit_losses.append([row[0],current_profit_loss])

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

    
    
    #print statments to test the correctness of the values
    print(round(average_diff,2))
    print(num_months)
    print(sum_profit_losses)
    print(month_max_diff)
    print(max_diff)
    print(month_min_diff)
    print(min_diff)
    
