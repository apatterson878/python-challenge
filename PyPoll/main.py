import os
import csv

county = []
candidate = []
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
for y in range(len(unique_candidate)): #range(0, 3)
    votes = 0
    # print(unique_candidate[idk])
    for z in range(len(candidate)): #range(0, 3521000)
        idk = (int(y) + 1)
        if candidate[z] == unique_candidate[y]:
            votes +=1 
            # print(f"{unique_candidate[y]}: {votes}")
    print(f"{unique_candidate[y]}: {votes}")
print("----------------------------")
print(f"Winner: ")
print("----------------------------")

# unique_candidate = list(set(candidate))

# print("")
# print("Election Results")
# print("----------------------------")
# print(f"Total Votes: {count}")
# print("----------------------------")
# for x in range(len(unique_candidate)):
#     print(f"{unique_candidate[x]}: ")
# print("----------------------------")
# print(f"Winner: ")
# print("----------------------------")