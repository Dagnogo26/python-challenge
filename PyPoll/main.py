import csv
import os

#Create list to add candidate info
candidate_name = []
total_percentage = []
voter_file = os.path.join('Resources', 'election_data.csv')

# read the file
with open(voter_file) as csvfile:

    datas = csv.reader(csvfile, delimiter=',')
    next(datas, None)
    print(datas)

    voter_id = 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

# calculate total votes
    for data in datas:
        voter_id += 1
        candidate_name.append(data[2])

# Calculate each candidate total votes and vote percentage        
    for name in candidate_name:
        if name == "Khan":
            cand1 = name.count("Khan")
            khan_count += cand1  
            khan_per = (khan_count / voter_id)
            khan_per_format = "{:.3%}".format(khan_per)
        elif name == "Correy":
            cand2 =  name.count("Correy") 
            correy_count += cand2
            correy_per = (correy_count / voter_id)
            correy_per_format = "{:.3%}".format(correy_per)
        elif name == "Li":
            cand3 =  name.count("Li") 
            li_count += cand3
            li_per = (li_count / voter_id)
            li_per_format = "{:.3%}".format(li_per)
        elif name == "O'Tooley":
            cand4 =  name.count("O'Tooley") 
            otooley_count += cand4  
            otooley_per = (otooley_count / voter_id)
            otooley_per_format = "{:.3%}".format(otooley_per)  
        total_count = [khan_count, correy_count, li_count, otooley_count ]
        names = ["Khan", "Correy", "Li", "O'tooley"]
        winner = total_count.index(max(total_count)) 


# Create new list with candidate name and their total vote
candidate_count = list(zip(names, total_count))  
       
#print results
print("Financial Analysis")
print("----------------------------")           
print(f"total votes : {voter_id}")
print(f"Khan : {khan_per_format} ({khan_count})")
print(f"Correy : {correy_per_format} ({correy_count})")
print(f"Li : {li_per_format} ({li_count})")
print(f"O'Tooley : {otooley_per_format} ({otooley_count})")
print(f"Winner : {candidate_count[winner][0]}")  


#put into text file

output_file = os.path.join('Analysis', 'Financial_analysis.txt')

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"total votes : {voter_id}")
    file.write("\n")
    file.write(f"Khan : {khan_per_format} ({khan_count})")
    file.write("\n")
    file.write(f"Correy : {correy_per_format} ({correy_count})")
    file.write("\n")
    file.write(f"Li : {li_per_format} ({li_count})")
    file.write("\n")
    file.write(f"O'Tooley : {otooley_per_format} ({otooley_count})")
    file.write("\n")
    file.write(f"Winner : {candidate_count[winner][0]}")

 