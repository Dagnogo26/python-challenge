import csv
import os

# Create list to the months, profit/losses and the change in profit/losses 
months = []
pl_info = [] 
pl_change = []


ceral_file = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(ceral_file) as csvfile:

    readers = csv.reader(csvfile, delimiter=',')
    next(readers, None)
    print(readers)

    totalmonths = 0
    totalamount = 0
    
    
# Compute numbers of months, the sum of amount   
    for reader in readers:
        totalmonths += 1
        totalamount = totalamount + int(reader[1])
        final_totamount = '${}'.format(totalamount)
        months.append(reader[0])
        pl_info.append(reader[1])

# Compute change in profit and loss, the max increase of pl change and min decrease of pl change
    for x in range(len(pl_info)):  
        change = int(pl_info[x]) - int(pl_info[x - 1])
        pl_change.append(change)
        greatest_change = '${}'.format(max(pl_change))
        greatest_decrease = '${}'.format(min(pl_change))
        max_increase_month = pl_change.index(max(pl_change)) 
        max_decrease_month = pl_change.index(min(pl_change)) 

# Calculate average change        
    def average(datachange):
        sum_change = 0 
        length = len(datachange)
        for x in datachange:
            sum_change = sum_change + x 
        avg =  sum_change / length
        avg_final = "{:.2f}".format(avg)
        avg_dol = '${}'.format(avg_final)
        return avg_dol 
datas = list(zip(months, pl_change))
      

pl_change.pop(0)

# print results
print("Financial Analysis")
print("----------------------------")
print(f"total months : {totalmonths}")
print(f"total amount : {final_totamount}") 
print(f"Average change : {average(pl_change)}") 
print(f"Greatest Increase in Profits : {datas[max_increase_month][0]} ({greatest_change})")  
print(f"Greatest decrease in Profits : {datas[max_decrease_month] [0]} ({greatest_decrease})")




output_file = os.path.join('Analysis', 'Financial_analysis.txt')

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"total months : {totalmonths}")
    file.write("\n")
    file.write(f"total amount : {final_totamount}")
    file.write("\n")
    file.write(f"Average change : {average(pl_change)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits : {datas[max_increase_month][0]} ({greatest_change})")
    file.write("\n")
    file.write(f"Greatest decrease in Profits : {datas[max_decrease_month] [0]} ({greatest_decrease})")

 




