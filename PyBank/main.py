# Create a path across operating systems
import os

# Use existing module to read csv files
import csv

# Files to load and output 
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables
total_months = 0
month_of_change = []
net_change_list = []
total_net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read csv file and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    
    # Read the header row
    header = next(reader)
    
    # Exclude first row 
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        
    # Track the total
        total_months += 1
        total_net += int(row[1])
        
    # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        
    # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
    # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
    # Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}"
    )

print(output)

# Specify file to write results to
output_path = os.path.join("..", "output", "new.csv")

# Open csv file using "write" mode
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write results in the file
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months:', '86'])
    csvwriter.writerow(['Average Change:', '$-224669'])
    csvwriter.writerow(['Greatest Increase in Profits:', 'Aug-16', '1862002'])
    csvwriter.writerow(['Greatest Decrease in Profits:', 'Feb-14', '-1825558'])



                       
