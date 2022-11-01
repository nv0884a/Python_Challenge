import os
import csv
from statistics import mean

header = "Financial Analysis"
dash = "----------------"
dates_sum = 0
value_sum = 0
values = []
changes = []
previous_month = 0
max_change = 0
max_change_date = ""
min_change = 0
min_change_date = ""


budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)
    
    for row in csv_reader:
        dates_sum = dates_sum + 1
        
        value_sum = value_sum + int(row[1])
        values.append(int(row[1]))

        if dates_sum > 1:
            change = int(row[1]) - previous_month
            changes.append(change)
            if change > max_change:
                max_change = change
                max_change_date = (row[0])

            if change < min_change:
                min_change = change
                min_change_date = (row[0])


        previous_month = int(row[1])


    average = mean(changes)

    print(header)
    print(dash)
    print("Total Months:",dates_sum)
    print("Total:","$",value_sum)
    print("Average Change:","$",average)
    print("Greatest Increase in profits:", max_change_date, max_change)
    print("Greatest Decrease in Profits",min_change_date, min_change)