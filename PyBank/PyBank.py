#The total number of months included in the dataset
#the net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#path
budget_data = os.path.join("..", "Documents", "GitHub", "DataClass", "Homework", "03-Python", "Instructions", "PyBank", "Resources", "budget_data.csv")

#open with and read csv header

with open(budget_data,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)




# define funtion and link it to budget_data as parameter
#def average (budget_data):

#totalMonths=len(budget_data[0])
#Net = int(budget_data[1])