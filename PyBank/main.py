import csv
import os

py_bank_csv_path = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(py_bank_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    header = csvreader.__next__

    next(csvreader)

    #initialize variables
    sum = 0
    num_months = 0
    changes = []
    current_change = 0

    # Loop through the data
    for row in csvreader:
        current_change = int(row[1])
        sum += current_change
        num_months += 1
        changes.append(current_change)

    print(num_months)
    print(sum)
    print(changes)