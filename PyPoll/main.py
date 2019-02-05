import os
import csv

county = []
candidate = []
uniquetesting = ["john", "joe", "john", "mel"]
unique_candidate = []

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
       county.append(row[1])
       candidate.append(row[2])
    
unique_candidate = list(set(candidate))

print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {count}")
print("----------------------------")
print(f"{unique_candidate[0]}: ")
print(f"{unique_candidate[1]}: ")
print(f"{unique_candidate[2]}: ")
print(f"{unique_candidate[3]}: ")
print("----------------------------")
print(f"Winner: ")
print("----------------------------")
