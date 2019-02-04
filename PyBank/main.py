import os
import csv

theday = []
price = []
months = 0

csvpath = os.path.join( "Resources", "budget_data.csv")
avgchange = 0.00

with open(csvpath, newline='') as csvfile:
    count = 0
    total = 0
    next(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # # Read the header row first (skip this step if there is no header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    
    for row in csvreader:
        
        count+=1
        total+= int(row[1])
        # print(int(row[1]))
        
        price.append(row[1])
        theday.append(row[0])
    
    lastprice = int(price[len(price)-1])
    firstprice = int(price[0])
    avgchange = (lastprice - firstprice)/85

    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgchange:.2f}")
    print("")

# Average change (lastnum-firstnum)/ 85
