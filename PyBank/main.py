#Open csv as read file 
import os 
import csv
file_to_load = os.path.join("budget_data.csv")
total_months = 0 
total_net = 0
change_values = []
total_net_change = 0
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
#         print(net_change)
        total_net_change += net_change
    print(total_net_change)
    average_change = round((total_net_change/85), 2)
    print(average_change)
#     print(f"Total months: {total_months}")
#     print(f"Total net profits/losses: {total_net}")
        
        
        