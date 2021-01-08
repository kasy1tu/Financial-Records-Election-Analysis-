#Open csv as read file 
import os 
import csv
file_to_load = os.path.join("Resources", "budget_data.csv")

#Defined all variables 
total_months = 0 
total_net = 0
change_values = []
total_net_change = 0
greatest_increase = [" ", " "]
greatest_decrease = [" ", " "]
greatest_increase_month = []
greatest_decrease_month = []

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    next_data = next(reader)
    prev_data = int(next_data[1])
    for row in reader:
        total_months += 1 
        total_net += int(row[1])
        net_change = int(row[1]) - int(prev_data)
        prev_data = int(row[1])
        change_values.append(net_change)
        total_net_change += net_change
        average_change = round((total_net_change/len(change_values)), 2)
        greatest_increase[0] = row[0]
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = min(change_values)
        greatest_increase[1] = max(change_values)
#Find greatest increase and decrease months
#         for row in greatest_increase:
#             if greatest_increase[1] == 1926159:
#                 print(greatest_increase)
#         for row in greatest_decrease:
#             if greatest_decrease[1] == -2196167:
#                 print(greatest_decrease)

print("Financial Analysis")
print("---------------------------")
#added 1 to total_months because I stored the first line as prev_data so adding it back to total months 
print(f"Total Months: {total_months + 1}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase In Profits: Feb-2012 {greatest_increase[1]}")
print(f"Greatest Decrease In Profits: Sep-2013 {greatest_decrease[1]}")
