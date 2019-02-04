import os
import csv

months = 0

csvpath = os.path.join( "Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:
    count = 0
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # # Read the header row first (skip this step if there is no header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    for row in csvreader:
        
        print(row[1])
        count+=1

    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print("")

    #print(row(row[1]))