import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Seperate Header from data
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    vote_count=0
    candidates=[]
    votes=[0,0,0,0]
    vote_percent=[0,0,0,0]
    
    #Loop through the CSV file
    for row in csvreader:
     
        #Count total votes
        vote_count=vote_count+1
    
    #Check and assign unique candidate names to the candidate list
    #Khan will be assiged index 0, Correy is index 1, Li is index 2
    #and O'Tooley is index 3
        if row[2] not in candidates:
            candidates.append(row[2])
     
        
     #Check for candidates name and assign votes to the correct index
        if row[2] =="Khan":
            votes[0]=votes[0]+ 1
        elif row[2] =="Correy":
            votes[1]=votes[1]+ 1
        elif row[2] =="Li":
            votes[2]=votes[2]+ 1
        else:
            votes[3]=votes[3]+ 1
    
    #Calculate and limit each vote percentage to 3 digits
    vote_percent[0]= round((votes[0]/vote_count)*100,3)
    vote_percent[1]= round((votes[1]/vote_count)*100,3)
    vote_percent[2]= round((votes[2]/vote_count)*100,3)
    vote_percent[3]= round((votes[3]/vote_count)*100,3)
   
    
   #Check for the candidate with the highest percentage
    if vote_percent[0]> vote_percent[1] and vote_percent[0]> vote_percent[2] and vote_percent[0]> vote_percent[3]:
        Winner=candidates[0]
    
    elif vote_percent[1]> vote_percent[0] and vote_percent[1]> vote_percent[2] and vote_percent[1]> vote_percent[3]:
        Winner=candidates[1]
        
    elif vote_percent[2]> vote_percent[0] and vote_percent[2]> vote_percent[1] and vote_percent[2]> vote_percent[3]:
        Winner=candidates[2]
        
    else:
        Winner=candidates[3]
    
    
    #Print out election results to terminal
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {vote_count}")
    print(f"-------------------------")
    print(f"{candidates[0]}: {vote_percent[0]}00% ({votes[0]})")
    print(f"{candidates[1]}: {vote_percent[1]}00% ({votes[1]})")
    print(f"{candidates[2]}: {vote_percent[2]}00% ({votes[2]})")
    print(f"{candidates[3]}: {vote_percent[3]}00% ({votes[3]})")
    print(f"-------------------------")
    print(f"Winner: {Winner}")
    print(f"-------------------------")



 # Output files
    output_file = os.path.join("Analysis", "Election_Results.txt")

    with open(output_file,"w") as file:
    
    # Write to text file to print Election Results 
        file.write(f"Election Results")
        file.write("\n")
        file.write(f"-------------------------")
        file.write("\n")
        file.write(f"Total Votes: {vote_count}")
        file.write("\n")
        file.write(f"-------------------------")
        file.write("\n")
        file.write(f"{candidates[0]}: {vote_percent[0]}00% ({votes[0]})")
        file.write("\n")
        file.write(f"{candidates[1]}: {vote_percent[1]}00% ({votes[1]})")
        file.write("\n")
        file.write(f"{candidates[2]}: {vote_percent[2]}00% ({votes[2]})")
        file.write("\n")
        file.write(f"{candidates[3]}: {vote_percent[3]}00% ({votes[3]})")
        file.write("\n")
        file.write(f"-------------------------")
        file.write("\n")
        file.write(f"Winner: {Winner}")
        file.write("\n")
        file.write(f"-------------------------")
