import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

total_months = 0
old_profit = 0
profit = []
profitdiff = []
datelist = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(","))

    next(csvreader)

    for row in csvreader:
        total_months += 1
        profit.append(int(row[1]))
        datelist.append(row[0])
        new_profit = int(row[1])

        if old_profit != 0:
            difference = (new_profit - old_profit)
            profitdiff.append(int(difference))
        old_profit = new_profit

    netprofits = sum(profit)
    totalmonths = total_months
    Avgdiff = sum(profitdiff) / len(profitdiff) 
    maxincrease = max(profitdiff)
    maxdecrease = min(profitdiff)
    maxindex = profitdiff.index(maxincrease) + 1
    minindex = profitdiff.index(maxdecrease) + 1
    maxdate = datelist[maxindex]
    mindate = datelist[minindex]

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(netprofits))
print("Average Change: $" + str(format(Avgdiff, ".2f")))
print("Greatest Increase in Profits: " + str(maxdate) + "($" + str(maxincrease) + ")")
print("Greatest Decrease in Profits: " + str(mindate) + "($" + str(maxdecrease) + ")")

output_path = os.path.join("Analysis")

f = open("analysis.txt", 'w')
f.write("Financial Analysis")
f.write("------------------------")
f.write = ("Total Months: " + str(totalmonths))
f.write = ("Total: $" + str(netprofits))
f.write = ("Average Change: $" + str(format(Avgdiff, ".2f")))
f.write = ("Greatest Increase in Profits: " + str(maxdate) + "($" + str(maxincrease) + ")")
f.write = ("Greatest Decrease in Profits: " + str(mindate) + "($" + str(maxdecrease) + ")")
f.close()

