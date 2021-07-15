import os
import csv

csvpath ='Resources/election_data.csv'
total_votes = 0
candidate = [] # Full List of candidates
candidate_Name = ""
candidate_votes =[]
percentage_votes =[]
#Open and read csv file
with open(csvpath) as csvfile:
#, newline = '', encoding = 'latin-1') as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=',')
    # Read header
    csv_header = next(csvfile)
    #print(f'Header:{csv_header}')

    # Read each row of data after the header
    for row in csv_reader:
       total_votes = total_votes + 1
       #candidate.append(row[2])
       #if row[2] not in candidate:
       #candidate.append(row[2])
       if row[2] not in candidate:  
          candidate.append(row[2]) 
          index = candidate.index(row[2])
          candidate_votes.append(1)
       else:
          index = candidate.index(row[2])
          candidate_votes[index] +=1
    for votes in candidate_votes:
          percentage =round((votes/total_votes)*100)
          percentage_format ="%.3f%%" % percentage
          percentage_votes.append(percentage_format)

    winner =max(candidate_votes)
    winner_index =candidate_votes.index(winner)
    winner_name = candidate[winner_index]

"""output_path = os.path.join(".","analysis","AnalysisReport_PyPoll.txt")
    with open(output_path, 'w', newline='') as csvwriter:
    csvwriter.write(f'Candidate: {candidate}')"""


print("Election Results")
print("------------------------")
print (f'Total Votes:  {total_votes}')
print("------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(percentage_votes[i])} ({str(candidate_votes[i])})")
print("--------------------------")
print(f"Winner: {winner_name}")
print("--------------------------")

output_path = os.path.join(".","analysis","AnalysisReport_PyPoll.txt")
with open(output_path, 'w', newline='') as Txtwriter:
  Txtwriter.write("Election Results")
  Txtwriter.write("\n")
  Txtwriter.write("------------------------")
  Txtwriter.write("\n")
  Txtwriter.write(f'Total Votes:  {total_votes}')
  Txtwriter.write("\n")
  Txtwriter.write("------------------------")
  Txtwriter.write("\n")
  for i in range(len(candidate)):
       Txtwriter.write(f"{candidate[i]}: {str(percentage_votes[i])} ({str(candidate_votes[i])})")
       Txtwriter.write("\n")
  Txtwriter.write("------------------------")
  Txtwriter.write("\n")
  Txtwriter.write(f"Winner: {winner_name}")
  Txtwriter.write("\n")
  Txtwriter.write("------------------------")

