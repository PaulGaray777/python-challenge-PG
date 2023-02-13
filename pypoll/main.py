# add our dependencies.
import csv
import os

# import modules
import pandas as pd

# set path to the source data file
elecData_csvPATH = "./resources/election_data.csv"

# set the output of the text file
textpath_results= "./analysis/pypoll_analysis.txt"

# preparing and setting variables
voterid_list = [] # list for voter id column (ballot id)
county_list = [] # list for the county column
candidates_list = [] # list for the candidate column
candidate_options = [] # list of candidates (names)
votespercandidate = [] # list total votes per candidate 
results_list =[] # list for each candidate receiving votes
resultspercentage_list = [] # list for total percentage votes per candidate

row_count=0
votes_winner=0
iteration1=0
iteration2=0
iteration3=0
iteration4=0


# open the csv file
with open(elecData_csvPATH) as csvfile:  
    csv_reader= csv.reader(csvfile)
    header = next(csv_reader)


    # read in each row and write data into lists
    for row in csv_reader:
        voterid=row[0] # set column 0 as voterid
        county=row[1] # set column 1 as county
        candidate=row[2] # set column 2 as candidate
        voterid_list.append(voterid) # add next line to list ballotId
        county_list.append(county) # add next line to list counties
        candidates_list.append(candidate) # add next line to list candidates

    # total number of votes cast   
    row_count= len(voterid_list) # count the total number of votes cast in the "Voter ID" column
    
    
candidate_options.append(candidates_list[0]) # pre loading for comparison

# first iteration is through the candidates_list to determine candidates voted for
for iteration1 in range(row_count-1):
    if candidates_list[iteration1+1] != candidates_list[iteration1] and candidates_list[iteration1+1] not in candidate_options:
        candidate_options.append(candidates_list[iteration1+1])

n=len(candidate_options)
    

# second iteration variable as index counter
for iteration2 in range(n): # range of the iteration depending on lenght of candidate_options
    votespercandidate.append(candidates_list.count(candidate_options[iteration2])) #Count total votes of Candidates and add to list total

# third iteration variable as index counter
loservotes=row_count # preloading loservoters with maximum votes for comparison

for iteration3 in range(n): 
    resultspercentage_list.append(f'{round((votespercandidate[iteration3]/row_count*100), 4)}%') # calculation percentage for each candidate
    if votespercandidate[iteration3]>votes_winner: # finding candidate with highest vote count
        winner=candidate_options[iteration3]
        votes_winner=votespercandidate[iteration3]
        
# fourth iteration variable as index counter
for iteration4 in range(n):
    results_list.append(f'{candidate_options[iteration4]}: {resultspercentage_list[iteration4]} ({votespercandidate[iteration4]})') # format list results_list 

results='\n'.join(results_list) # results to be writed into the text analysis file and printed for checking results

# final results generation

analysis=f'\
Election Results\n\
------------------------------------------\n\
Total Votes: {row_count}\n\
------------------------------------------\n\
{results}\n\
------------------------------------------\n\
Winner: {winner} \n\
------------------------------------------\n'

print(analysis) 


# write changes to csv
with open(textpath_results, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------------------------------\n")
    file.write("Total Votes: %d\n" % row_count)
    file.write("------------------------------------------\n")
    file.write(f'{results}\n')
    file.write("------------------------------------------\n")
    file.write(f'Winner: {winner} \n')
