import os
import csv
csvpath = os.path.join("election_data.csv")
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)