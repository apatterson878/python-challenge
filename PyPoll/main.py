import os
import csv

county = []
candidate = []
unique_candidate = []
votestorage = 0
percentofvote = 0.00
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

#making text file
file= open("Election Results.txt","w+")
file.write("\n")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {count}\n")
file.write("----------------------------\n")
#####
votes = 0
winner = unique_candidate[0]
for y in range(len(unique_candidate)): 
    votes = 0
    
    for z in range(len(candidate)): 
        
        if candidate[z] == unique_candidate[y]:
            votes +=1 
            
    percentofvote = round(float((votes / count)*100),3)
    

    if votes > votestorage:
        winner = unique_candidate[y]
        votestorage = votes
    

    
    print(f"{unique_candidate[y]}:{percentofvote}% ({votes})") 
    file.write(f"{unique_candidate[y]}: {percentofvote}% ({votes})\n") 

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

file.write("----------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("----------------------------\n")
file.close() 