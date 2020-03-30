import os
import csv
# Lookup Election Data file
pypoll_csv = os.path.join('.', 'Resources','election_data.csv')

# Set voter count variable
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    voter=0

    for row in csvreader:
        voter +=1

# Set categorize votes for each candidate
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    candidates_all = []
    count = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for row in csvreader:
        candidates_all.append(row[2])

with open(pypoll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        candidate = (row[2])
        count = count + (candidate.count("Khan"))
        count2 = count2 + (candidate.count("Correy"))
        count3 = count3 + (candidate.count("Li"))
        count4 = count4 + (candidate.count("O'Tooley"))
# Set vote percentages
    Percent_Khan = (count/voter)*100
    Percent_Correy = (count2/voter)*100
    Percent_Li = (count3/voter)*100
    Percent_Tooley = (count4/voter)*100

# Create lists of candiates and vote counts
candidates = ["O'Tooley", "Correy", "Li", "Khan",]
counts = [count, count2, count3, count4,]

# Merge lists into tuples
voter_count = zip(candidates, counts)

# Find highest voter count
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    winner = max(counts)

    for row in voter_count:
        row[1] == winner
        winner_name = row[0]

# Print results and export txt file
print("Election Results")
print(f"Total Votes: {voter}")
print(f"Khan: {str(Percent_Khan)}% ({(count)})")
print(f"Correy: {str(Percent_Correy)}% ({(count2)})")
print(f"Li: {str(Percent_Li)}% ({(count3)})")
print(f"O'Tooley {str(Percent_Tooley)}% ({(count4)})")
print(f"Winner: {winner_name}")

file = open('PollOutput.txt', 'w')

file.write("Election Result")
file.write(f"Total Votes: {voter}")
file.write(f"Khan: {str(Percent_Khan)}% ({(count)})")
file.write(f"Correy: {str(Percent_Correy)}% ({(count2)})")
file.write(f"Li: {str(Percent_Li)}% ({(count3)})")
file.write(f"O'Tooley {str(Percent_Tooley)}% ({(count4)})")
file.write(f"Winner: {winner_name}")
file.close()