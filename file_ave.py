# file_ave.py
# read integers from text file NUMBERS.DAT, compute and display average

infile = open("NUMBERS.DAT", "r")

lines = infile.readlines()

# initialize variables
count = 0
total = 0

for num in lines: # loop through lines
    total = total + int(num) # add to total
    count = count + 1 # add to number of integers

# compute average
average = total / count

# display average
print(average)

# close file
infile.close()

