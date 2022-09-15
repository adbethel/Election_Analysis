# Election_Analysis
Python coding

                                        Election Analysis Review:


Overview of Election Audit 
  The purpose of this election audit analysis is to create a visual summary of the results of an election taking place between three counties. The analysis created a code that summaries the winner based on the votes they received, the percentage of votes between each candidate, and the county that submitted the most votes. 



Election Audit Results:
See below for a bulleted explanation of each election result:

Election Results
-	Total Votes: 369,711: Total votes submitted in the election
-------------------------

County Votes: The total votes submitted stratified by county
-	Jefferson: 10.5% (38,855)
-	Denver: 82.8% (306,055)
-	Arapahoe: 6.7% (24,801)
-------------------------
Largest County Turnout: Denver
The number of votes each candidate received by percentage and by number: 

-	Charles Casper Stockham: 23.0% (85,213)
-	Diana DeGette: 73.8% (272,892)
-	Raymon Anthony Doane: 3.1% (11,606)
The winner of the election indicated by the number of votes received and the percentage of votes received: 
-	Winner: Diana DeGette
-	Winning Vote Count: 272,892
-	Winning Percentage: 73.8%



Election Audit Summary:
	This script can be used as a template for different elections in the future by following simple modifications based  on the changes in demographics. For example, if the counties in a future election is different, you can add or remove county names, voter count and candidates by importing a different csv file, but also, you would be able to see other information that may be important to understanding election turnout. You can modify the script to show smallest county turnout, an important factor that can show areas of opportunity for candidates to canvas in future elections. You can do this by modifying the script  in the following way:
#2 smallest_county_turnout_name = ""
smallest_county_turnout_vote = 0
smallest_county_percentage = 0

Then write an if statement to determine the county with the smallest voter turnout:
if (countyvotes > smallest_county_turnout_vote) and (countyvote_percentage > smallest_county_percentage):
            smallest_county_turnout_name = county
            smallest_county_turnout_vote = countyvotes
            smallest_county_percentage = countyvote_percentage

#7: smallest_county_print = (
        f"-------------------------\n"
        f"Smallest County Turnout: {smallest_county_turnout_name}\n"
        f"-------------------------\n"
    )
    print(smallest_county_print)


![image](https://user-images.githubusercontent.com/112285856/190286814-6191f90c-fe5c-4269-bd09-fc68507a3d6d.png)
