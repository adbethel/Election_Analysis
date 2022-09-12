import csv
import os
file_to_load = os.path.join("Results", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# candidate Options
candidate_options = []

# Candidate votes 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
     # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in CSV file.
    for row in file_reader:
        total_votes += 1
    
        #Print candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidated
            candidate_options.append(candidate_name)

            #Begin tracking that candidate vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate' count
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Caldulate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes.
        print(f"{candidate_name}: recieved {vote_percentage}% of the vote.")
    
        #Determine the winning candidate by the number and percentage of votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage 
            #3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

print(winning_candidate_summary)

#Print the total votes
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")





#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. the percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.


#Choose the file








