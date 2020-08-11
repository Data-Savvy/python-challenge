import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    Months_count=0
    Total_count=0
    Change=[]
    P_L=[]
    M_Y=[]
    Max = 0 
    Min = 0
    
    #Calculate total months, profits/losses, and create new comparable lists
    for row in csvreader:
        Months_count= Months_count+1
        Total_count = Total_count + int(row[1])
        P_L.append(row[1])
        M_Y.append(row [0])
    
    #Calculate Change from month to month and Min and Max values
    for i in range (len(P_L)-1):
        c = float(P_L[i+1]) - float(P_L[i])
        Change.append(c)
        if c > Max:
            Max = int(c)
        
        elif c < Min:
            Min = int(c)
   
    #Change is will be seen next month so we add 1 to the index
    Max_date =M_Y[Change.index(Max)+1]
    Min_date =M_Y[Change.index(Min)+1]
  
    
    #Calculate Average change
    average_change = round(sum(Change)/len(Change),2)
    
    #Print finicial statements out
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months:  {Months_count}")
    print(f"Total: {Total_count}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {Max_date} (${Max})")
    print(f"Greatest Decrease in Profits: {Min_date} (${Min})" )
    
    
    
    # Output files
    output_file = os.path.join("Analysis", "Financial_Analysis_Summary.txt")

    with open(output_file,"w") as file:
    
    # Write methods to print to Financial_Analysis_Summary 
        file.write("Financial Analysis")
        file.write("\n")
        file.write("-------------------")
        file.write("\n")
        file.write(f"Total Months:  {Months_count}")
        file.write("\n")
        file.write(f"Total: {Total_count}")
        file.write("\n")
        file.write(f"Average Change: ${average_change}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {Max_date} (${Max})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {Min_date} (${Min})" )
    
    