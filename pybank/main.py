# add dependencies.
import csv
import os

# import modules
import pandas as pd


# set path to the source data file
budData_csvPATH = "./resources/budget_data.csv"


# set the output of the text file
textPATH_results= "./analysis/pybank_analysis.txt"

# set variables
tot_months = 0
tot_revenue = 0
revenue = []
old_revenue = 0
changing_month = []
change_in_revenue = 0
greatest_dec= ["", 9999999]
greatest_inc = ["", 0]
change_in_revenue_list = []
average_revenue = 0

# start analysis

# open the csv file
with open(budData_csvPATH) as csvfile:  
    csv_reader= csv.reader(csvfile)

    # loop through to find total months
    header=next(csv_reader)
    for row in csv_reader:

        # count the total of months
        tot_months += 1

        # calculate the total revenue 
        tot_revenue = tot_revenue + float(row[1])
       
        # calculate the average change in revenue 
        change_in_revenue = float(row[1])- old_revenue
        old_revenue = float(row[1])
        change_in_revenue_list = change_in_revenue_list + [change_in_revenue]
        changing_month = [changing_month] + [row[0]]
       

        # set greatest increase in revenue
        if change_in_revenue>greatest_inc[1]:
            greatest_inc[1]= change_in_revenue
            greatest_inc[0] = row[0]

        # set greatest decrease in revenue
        if change_in_revenue<greatest_dec[1]:
            greatest_dec[1]= change_in_revenue
            greatest_dec[0] = row[0]
    average_revenue = sum(change_in_revenue_list)/len(change_in_revenue_list)

# write changes to csv file, in the output text file
with open(textPATH_results, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % tot_months)
    file.write("Total Revenue: $%d\n" % tot_revenue)
    file.write("Average Revenue Change $%d\n" % average_revenue)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_inc[0], greatest_inc[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_dec[0], greatest_dec[1]))
    
# print the results to easy access in the jupyter notebook
    print("Financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" % tot_months)
    print("Total Revenue: $%d\n" % tot_revenue)
    print("Average Revenue Change $%d\n" % average_revenue)
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_inc[0], greatest_inc[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_dec[0], greatest_dec[1]))