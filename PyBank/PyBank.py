#The total number of months included in the dataset
#the net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#path
budget_data = os.path.join("budget_data.csv")

#varibable tracking
totalMonths = 0
profitTotal = 0

oldProfit = 0
profitChange = 0
greatestIncrease = ['',0]
greatestDecrease = ['',99999999]

 #open with and read csv header

with open("budget_data.csv","r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #loop through rows of data
    for row in csvreader:

        #totals
        totalMonths = totalMonths + 1
        profitTotal = profitTotal + int(row[1])
        #print (row)

        #changes
        profitChange = int(row[1]) - oldProfit
        #print (oldProfit)

print ("Financial Analysis")
print ("-----------------------")
print ("Total Months: " + str(totalMonths))
print ("Total Profit: " + "$" + str(profitTotal)

        #increase
        if profitChange > greatestIncrease[1]
            greatestIncrease[1] = profitChange
            greatestIncrease[0] = row[0]
            
        if profitChange < greatestDecrease[1]
            greatestDecrease[1] = profitChange
            greatestDecrease[0] = row[0]

#average
totalAvg = profitTotal / totalMonths

print ("Total Change: " + "$" + str(round(sum(profitChange) / totalMonths ,2))
print ("Greatest Increase: " + str(greatestIncrease[0]) + " ($" + str(greatestIncrease[1]) + ")")
print ("Greatest Decrease: " + str(greatestDecrease[0]) + " ($" + str(greatestDecrease[1]) + ")")