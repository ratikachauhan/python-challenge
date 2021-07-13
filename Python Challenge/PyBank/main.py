#import dependencies
import os
import csv

#read csv path
csvpath =  'Resources/budget_data.csv'
#csvpath = os.path.join("Resources", "cereal.csv")

# Intilize variables
month = []
total = []
change =[]
#Open and read csv file
with open(csvpath) as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=',')
    # Read header
    csv_header = next(csvfile)
    #print(f'Header:{csv_header}')


 # Read each row of data after the header
    for row in csv_reader:
        #print(row)
        month.append(row[0])
        total.append(int(row[1]))
    for i in range(len(total)-1):
        change.append (total[i+1]-total[i])

total_months =len(month)
total =sum(total)
average_change = round(sum(change)/len(change),2)

greatest_increase = max(change)
month_increase_index = change.index(greatest_increase)+1
month_greatest_increase =month[month_increase_index]

greatest_decrease = min (change)
month_decrease_index = change.index(greatest_decrease)+1
month_greatest_decrease =month[month_decrease_index]

#Print Financial Analysis
print("Financial Analysis")
print("------------------------")
print (f'Total Months: {total_months}')
print (f'Total: ${total}')
print (f'Average  Change: ${average_change}')
print (f'Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})')
print (f'Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})')

#Write File
output_path = os.path.join(".","output.txt")
with open(output_path, 'w', newline='') as csvwriter:
    csvwriter.write("Financial Analysis")
    csvwriter.write("\n")
    csvwriter.write("------------------------")
    csvwriter.write("\n")
    csvwriter.write(f'Total Months: {total_months}')
    csvwriter.write("\n")
    csvwriter.write(f'Total: ${total}')
    csvwriter.write("\n")
    csvwriter.write(f'Average  Change: ${average_change}')
    csvwriter.write("\n")
    csvwriter.write(f'Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase})')
    csvwriter.write("\n")
    csvwriter.write(f'Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease})')



