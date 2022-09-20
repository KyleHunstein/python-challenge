# Imports
import os
import csv
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
PyBank_analysis = os.path.join('Analysis', 'Bank_Results.txt')

# Lists for data
total_months = []
net_total = []
greatest_increase = []
greatest_decrease = []
average_change_list = []
average_change = []

# List Creations
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        total_months.append(row[0])
        net_total.append(int(row[1]))

# Average
for i in range(len(net_total)-1):
        average_change_list.append(net_total[i + 1] - net_total[i])
average_change= round(sum(average_change_list)/len(average_change_list),2)

# Min/Max
greatest_increase = max(average_change_list)
greatest_decrease = min(average_change_list)


# Printing Outcome
print("Financial Analysis")
print("-------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")

#amount_of_months = len(total_months)

# Text File Creation

f = open(PyBank_analysis, "w")
print(("Financial Analysis"), file=f)
print(("-------------"), file=f)
print((f"Total Months: {len(total_months)}"), file=f)
print((f"Total: ${sum(net_total)}"), file=f)
print((f"Average Change: ${average_change}"), file=f)
print((f"Greatest Increase in Profits: {greatest_increase}"), file=f)
print((f"Greatest Decrease in Profits: {greatest_decrease}"), file=f)
f.close()