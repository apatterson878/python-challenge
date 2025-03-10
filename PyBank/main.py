import os
import csv

theday = []
price = []
months = 0
greatprice = 0

csvpath = os.path.join( "Resources", "budget_data.csv")
avgchange = 0.00

with open(csvpath, newline='') as csvfile:
    count = 0
    total = 0
    next(csvfile)
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # # Read each row of data after the header  
    for row in csvreader:
        
        count+=1
        total+= int(row[1])
        
        price.append(row[1])
        theday.append(row[0])

        greatpriceday = theday[0]
        worstpriceday = theday[0]

    greatprice = int(price[0]) - int(price[1])
    worstprice = int(price[0]) - int(price[1])
    
    for x in range(len(price)-1):
        idk = (int(x) + 1)
        pricechange = int(price[idk]) - int(price[x])
        if pricechange > greatprice:
            greatprice = pricechange
            greatpriceday = theday[idk]

        if pricechange < worstprice:
            worstprice = pricechange
            worstpriceday = theday[idk]
      
    #Finding the first price and last price for avg change
    lastprice = int(price[len(price)-1])
    firstprice = int(price[0])
    print(firstprice)
    print(lastprice)

    avgchange = (lastprice - firstprice)/85   

    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgchange:.2f}")
    print(f"Greatest Increase in Profits: {greatpriceday} ${greatprice}")
    print(f"Greatest Decrease in Profits: {worstpriceday} ${worstprice}")
    print("----------------------------")
    print("")

#Creating the text file

file= open("Financial Analysis.txt","w+")

file.write("\n")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {count}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${avgchange:.2f}\n")
file.write(f"Greatest Increase in Profits: {greatpriceday} ${greatprice}\n")
file.write(f"Greatest Decrease in Profits: {worstpriceday} ${worstprice}\n")
file.write("----------------------------\n")
file.write("\n")

file.close() 
