import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates_raw = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidates_raw.append(row[2])

    khan_total = candidates_raw.count('Khan')
    khan_percent = (khan_total / total_votes)
    khan_percent_format = "{:.0%}".format(khan_percent)

    correy_total = candidates_raw.count('Correy')
    correy_percent = (correy_total / total_votes)
    correy_percent_format = "{:.0%}".format(correy_percent)

    li_total = candidates_raw.count('Li')
    li_percent = (li_total / total_votes)
    li_percent_format = "{:.0%}".format(li_percent)

    otool_total = candidates_raw.count("O'Tooley")
    otool_percent = (otool_total / total_votes)
    otool_percent_format = "{:.0%}".format(otool_percent)

    most_votes = max(khan_total, li_total, correy_total, otool_total)

    votes = {
        "Khan": [khan_total],
        "Correy": [correy_total],
        "Li": [li_total],
        "O'Tooley": [otool_total]
    }

    key_list = list(votes.keys())
    val_list = list(votes.values())

    for number in val_list:
        if number[0] == most_votes:
            winner = key_list[val_list.index(number)]
            
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes))
print("---------------------------")
print("Khan: " + str(khan_percent_format) + " (" + str(khan_total) + ")")
print("Correy: " + str(correy_percent_format) + " (" + str(correy_total) +")")
print("Li: " + str(li_percent_format) + " (" + str(li_total) + ")")
print("O'Tooley: " + str(otool_percent_format) + " (" + str(otool_total) + ")")
print("---------------------------")
print("Winner: " + str(winner))
print("---------------------------")


output_path = os.path.join("Analysis", "analysis.txt")
f = open(output_path, 'w')
f.write("Election Results \n")
f.write("--------------------------- \n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("--------------------------- \n")
f.write("Khan: " + str(khan_percent_format) + " (" + str(khan_total) + ")\n")
f.write("Correy: " + str(correy_percent_format) + " (" + str(correy_total) +")\n")
f.write("Li: " + str(li_percent_format) + " (" + str(li_total) + ")\n")
f.write("O'Tooley: " + str(otool_percent_format) + " (" + str(otool_total) + ")\n")
f.write("---------------------------\n")
f.write("Winner: " + str(winner) + "\n")
f.write("---------------------------\n")