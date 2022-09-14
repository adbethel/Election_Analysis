print("Hello World") 
counties = ("Arapahoe","Denver","Jefferson")
type(True)
my_votes = int(input("how many votes did you get in the election"))
total_votes = int(input("what is the total votes in the election"))
percentage_votes = (my_votes / total_votes) * 100
print("I recieved" + str(percentage_votes)+ "% of the total votes")
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
for county in counties:
    print(county)
    