import os
import csv


csvpath = os.path.join( "Resources", "election_data.csv")


with open(csvpath, newline='') as csvfile:
    count = 0
    # next(csvfile)

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
       count+=1
       
print(count)


print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {count}")
print("----------------------------")