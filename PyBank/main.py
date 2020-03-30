import os
import csv
# Lookup Budget Data file
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Set total number of months variable
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    months = 0
    
    for row in csvreader:
        months +=1

# Find total Profit/Losses    
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)  
    dates = []
    total_count = []

    for row in csvreader:
        total_count.append((int(row[1])))
        dates.append(row[0])

    for line in total_count:
        total = sum(total_count)

# Find Change in Profit/Losses
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)  

    # Make an empty list for change in revenue
    revenue_change = [0]
    for deck in range(len(total_count)-1):
# Add the next value to the revenure change list
        revenue_change.append(int(total_count[deck+1] - int(total_count[deck])))
        
average_change = (sum(revenue_change)/85)

# Merge Date list and Revenue Change list
revchange = zip(dates, revenue_change)

# Pull Greatest Increase in Profits
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)  
    maxinc = (max(revenue_change))
    mininc = (min(revenue_change))
    
    for inc in revchange:
        if inc[1] == maxinc:
            maxinc_date = inc[0]
# Pull Greatest Decrease in Profits
        elif inc[1] == mininc:
            mininc_date = inc[0]

#Print output and export file
print("Financial Analysis")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {maxinc_date} (${maxinc})")
print(f"Greatest Decrease in Profits: {mininc_date} (${mininc})")

file = open('FinancialAnalysis.txt', 'w')

file.write("Financial Analysis")
file.write(f"Total Months: {months}")
file.write(f"Total: ${total}")
file.write(f"Average Change: ${average_change}")
file.write(f"Greatest Increase in Profits: {maxinc_date} (${maxinc})")
file.write(f"Greatest Decrease in Profits: {mininc_date} (${mininc})")
file.close()