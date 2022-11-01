import os
import csv

total_votes = 0
candidates = {"Charles Casper Stockham": 0, "Diana DeGette": 0, "Raymon Anthony Doane": 0}
percentage1 = 0
percentage2 = 0
percentage3 = 0


election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_file)
    


    for row in csv_reader:
        total_votes = total_votes + 1
        
        
        candidates[row[2]] = candidates[row[2]] + 1

    percentage1 = (candidates["Charles Casper Stockham"]/total_votes*100)
    percentage2 = (candidates["Diana DeGette"]/total_votes*100)
    percentage3 = (candidates["Raymon Anthony Doane"]/total_votes*100)

    print("Election Results")
    print("-----------------")
    print(total_votes)
    print("-----------------")
    print(candidates)
    print(percentage1,'%', percentage2,'%' ,percentage3,'%')
    print("-----------------")

    if candidates["Charles Casper Stockham"] > candidates["Diana DeGette"] and candidates["Charles Casper Stockham"] > candidates["Raymon Anthony Doane"]:
        print("Winner: Charles Casper Stockham")

    elif candidates["Diana DeGette"]  > candidates["Charles Casper Stockham"] and candidates["Diana DeGette"] > candidates["Raymon Anthony Doane"]:
        print("Winner: Diana DeGette")

    elif candidates["Raymon Anthony Doane"]  > candidates["Charles Casper Stockham"] and candidates["Raymon Anthony Doane"] > candidates["Diana DeGette"]:
        print("Winner: Raymon Anthony Doane")

    print("------------------")

