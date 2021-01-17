# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a variable for total votes
total_votes = 0
# Initialize a variable for candidate name
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Determine winning vote count and candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the headers
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Increment the total_votes
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            # Candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add to Candidate's vote count
        candidate_votes[candidate_name] +=1  
        

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        
        
        
        
#print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
   

#print candidate's vote
#print(candidate_votes)

# Print candidate name
#print(candidate_options)

# Print total votes
#print(total_votes)


    
    