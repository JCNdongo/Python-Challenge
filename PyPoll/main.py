# Create a path across operating systems
import os

# Use existing module to read csv files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Define variables
Total_Votes = 0
Candidates_List = []
Winner = []


# Open csv file to compute total months excluding first row with headers
with open(csvpath) as csvfile: 
    csvreader = csv.DictReader(csvfile, delimiter=',')
    Total_Votes = len(list(csvreader))


  # Generate Output Summary
output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {Total_Votes}\n"
    f"Candidates: {Candidates_List}\n"
    f"Winner: {Winner}\n" 
    )

print(output)

# Specify file to write results to
output_path = os.path.join("output", "new.csv")

# Open csv file using "write" mode
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write results in the file
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', '369711'])
    csvwriter.writerow(['Candidates:', ''])
    csvwriter.writerow(['Winner:', ''])
   